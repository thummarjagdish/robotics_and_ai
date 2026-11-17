"""Detailed Python companion to updated_transformer_from_scratch_code.ipynb.

This file explains the notebook's German-to-English Multi30k workflow: data,
tokenization, vocabularies, Transformer layers, training, and translation.
Place the six Multi30k .gz files in the local data/ folder before running.
"""

# Standard library imports: included with Python.
import gzip  # Read compressed text files directly, without manually extracting them.
import math  # Supplies sqrt/log/exp operations used in attention and loss reporting.
import random  # Seed Python's random number generator.
import time  # Measure how long training and validation take.
from collections import Counter  # Count vocabulary token frequencies.
from pathlib import Path  # Build portable file paths.
from typing import Callable, Dict, List, Optional, Tuple  # Document data and function types.
from urllib.request import urlretrieve  # Download dataset files if the optional setting is enabled.

# Third-party imports: PyTorch implements the model; tqdm draws progress bars.
import torch  # Tensor math, device handling, and automatic differentiation.
import torch.nn as nn  # Neural network layers and base class Module.
import torch.optim as optim  # Parameter update algorithms, including Adam.
from torch.nn.utils.rnn import pad_sequence  # Pad variable-length sentences in each batch.
from torch.utils.data import DataLoader, Dataset  # Dataset protocol and mini-batch iteration.
from tqdm import tqdm  # Show progress while training or validating.

# Set reproducible random seeds. This improves repeatability; GPU operations may
# still vary slightly across hardware or library versions.
SEED = 123
random.seed(SEED)  # Seed Python random operations.
torch.manual_seed(SEED)  # Seed PyTorch's CPU random generator.
torch.backends.cudnn.deterministic = True  # Prefer deterministic CUDA algorithms.

# Choose CUDA only when the current PyTorch environment can access it; otherwise CPU.
# Models and tensors must also be moved to DEVICE later with .to(DEVICE).
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)
if device.type == "cuda":
    print("GPU:", torch.cuda.get_device_name(0))  # Name the first CUDA GPU.

# The notebook attempted to load spaCy models and fell back to split() if missing.
def load_spacy_model(model_name: str):
    """Load a spaCy model; return None if spaCy or that language model is missing."""
    try:
        import spacy  # Import inside the function so spaCy remains optional.
        return spacy.load(model_name)  # Return the loaded German/English tokenizer pipeline.
    except Exception:
        print(f"Could not load {model_name}; using whitespace tokenization instead.")
        print(f"Install it with: python -m spacy download {model_name}")
        return None  # None tells tokenize_de/tokenize_en to use the fallback.


spacy_de = load_spacy_model("de_core_news_sm")  # Small German tokenizer model.
spacy_en = load_spacy_model("en_core_web_sm")  # Small English tokenizer model.


def tokenize_de(text: str) -> List[str]:
    """Lowercase a German sentence and return its token strings."""
    if spacy_de is not None:
        return [token.text.lower() for token in spacy_de.tokenizer(text)]
    return text.lower().strip().split()  # Simple fallback; punctuation can remain attached.


def tokenize_en(text: str) -> List[str]:
    """Lowercase an English sentence and return its token strings."""
    if spacy_en is not None:
        return [token.text.lower() for token in spacy_en.tokenizer(text)]
    return text.lower().strip().split()  # Fallback if spaCy/model is unavailable.


# The notebook used the Colab path /content/data. This companion uses a data
# directory next to this .py file, which works on a local Windows installation.
SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)  # Create folder if needed; does not download files.
train_de_path = str(DATA_DIR / "train.de.gz")
train_en_path = str(DATA_DIR / "train.en.gz")
val_de_path = str(DATA_DIR / "val.de.gz")
val_en_path = str(DATA_DIR / "val.en.gz")
test_de_path = str(DATA_DIR / "test_2016_flickr.de.gz")
test_en_path = str(DATA_DIR / "test_2016_flickr.en.gz")
# These are the six files the notebook downloaded with wget. Put them in data/.
MULTI30K_URLS = {
    "train.de.gz": "https://github.com/multi30k/dataset/raw/master/data/task1/raw/train.de.gz",
    "train.en.gz": "https://github.com/multi30k/dataset/raw/master/data/task1/raw/train.en.gz",
    "val.de.gz": "https://github.com/multi30k/dataset/raw/master/data/task1/raw/val.de.gz",
    "val.en.gz": "https://github.com/multi30k/dataset/raw/master/data/task1/raw/val.en.gz",
    "test_2016_flickr.de.gz": "https://github.com/multi30k/dataset/raw/master/data/task1/raw/test_2016_flickr.de.gz",
    "test_2016_flickr.en.gz": "https://github.com/multi30k/dataset/raw/master/data/task1/raw/test_2016_flickr.en.gz",
}
DOWNLOAD_DATASET = False  # Set True if this script should download missing files when run.


def download_multi30k() -> None:
    """Download the six dataset files, matching the notebook's wget setup cell."""
    for filename, url in MULTI30K_URLS.items():
        output_path = DATA_DIR / filename  # Save each downloaded file in the local data folder.
        if output_path.exists():  # Skip files that are already present.
            continue
        print(f"Downloading {filename} ...")
        urlretrieve(url, output_path)  # Fetch URL contents and write them to output_path.


class Multi30kDataset(Dataset):
    """Load paired German/English lines from two gzip files and tokenize on request."""

    def __init__(self, src_file: str, trg_file: str,
                 src_transform: Optional[Callable[[str], List[str]]] = None,
                 trg_transform: Optional[Callable[[str], List[str]]] = None):
        self.src_data = self.load_data(src_file)  # Read German source lines.
        self.trg_data = self.load_data(trg_file)  # Read corresponding English target lines.
        # Each source must have one paired target at the same line index.
        assert len(self.src_data) == len(self.trg_data), "Source and target files must have same length."
        self.src_transform = src_transform  # Save optional German tokenizer.
        self.trg_transform = trg_transform  # Save optional English tokenizer.

    def load_data(self, file_path: str) -> List[str]:
        """Read a gzip-compressed UTF-8 file and return its lines as strings."""
        with gzip.open(file_path, "rt", encoding="utf-8") as f:
            return f.readlines()  # One sentence per list item; text mode decodes UTF-8.

    def __len__(self) -> int:
        """Return the number of paired examples so DataLoader knows dataset size."""
        return len(self.src_data)

    def __getitem__(self, idx: int) -> Dict[str, List[str]]:
        """Fetch one pair, strip line endings, optionally tokenize, then return both sides."""
        src_sentence = self.src_data[idx].strip()
        trg_sentence = self.trg_data[idx].strip()
        if self.src_transform:  # Convert raw German text into token strings.
            src_sentence = self.src_transform(src_sentence)
        if self.trg_transform:  # Convert raw English text into token strings.
            trg_sentence = self.trg_transform(trg_sentence)
        return {"src": src_sentence, "trg": trg_sentence}  # Named keys clarify each language.


# Special tokens are reserved at the start of both vocabularies and get stable IDs.
PAD_TOKEN = "<pad>"  # Padding added to shorter sentences in a batch.
SOS_TOKEN = "<sos>"  # Start-of-sentence marker; starts decoder generation.
EOS_TOKEN = "<eos>"  # End-of-sentence marker; stops generation.
UNK_TOKEN = "<unk>"  # Substitute for a word that was not in the vocabulary.
SPECIAL_TOKENS = [PAD_TOKEN, SOS_TOKEN, EOS_TOKEN, UNK_TOKEN]


def create_vocab(tokenized_sentences: List[List[str]], special_tokens: List[str],
                 min_freq: int = 1) -> Dict[str, int]:
    """Map words to integer IDs; reserve special IDs and optionally drop rare words."""
    vocab = {token: idx for idx, token in enumerate(special_tokens)}  # IDs 0,1,2,3 in order.
    counter = Counter(token for sent in tokenized_sentences for token in sent)  # Count all words.
    for token, freq in counter.items():  # Visit each distinct token and its frequency.
        if freq >= min_freq and token not in vocab:  # Retain words meeting threshold only.
            vocab[token] = len(vocab)  # Current size is the next free integer ID.
    
    return vocab  # Used by embeddings to convert token IDs into vectors.


def build_datasets_and_vocabs():
    """Load train/validation/test data and build language vocabularies from training data."""
    train_data = Multi30kDataset(train_de_path, train_en_path, tokenize_de, tokenize_en)
    val_data = Multi30kDataset(val_de_path, val_en_path, tokenize_de, tokenize_en)
    test_data = Multi30kDataset(test_de_path, test_en_path, tokenize_de, tokenize_en)
    # Build vocabularies using training sentences only, avoiding validation/test data leakage.
    train_de_tokenized = [tokenize_de(s.strip()) for s in train_data.src_data]
    train_en_tokenized = [tokenize_en(s.strip()) for s in train_data.trg_data]
    src_vocab = create_vocab(train_de_tokenized, SPECIAL_TOKENS)  # German word -> ID.
    trg_vocab = create_vocab(train_en_tokenized, SPECIAL_TOKENS)  # English word -> ID.
    print(src_vocab)  # Optional: print the German vocabulary for inspection.
    print(trg_vocab)  # Optional: print the English vocabulary for inspection.
    return train_data, val_data, test_data, src_vocab, trg_vocab


# ---------------------------------------------------------------------------
# Transformer model
# ---------------------------------------------------------------------------

class PositionalEncoding(nn.Module):
    """Add fixed sine/cosine vectors so attention can distinguish token positions."""
    def __init__(self, d_model: int, max_len: int = 5000):
        super().__init__()  # Initialize PyTorch's Module bookkeeping.
        pe = torch.zeros(max_len, d_model)  # Reserve one positional vector per position.
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)  # Column of positions.
        # Different dimensions use different wavelengths; even/odd dimensions pair sine/cosine.
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)  # Fill even feature indices.
        pe[:, 1::2] = torch.cos(position * div_term)  # Fill odd feature indices.
        pe = pe.unsqueeze(0)  # Shape [1,max_len,d_model], broadcasts across batch dimension.
        self.register_buffer("pe", pe)  # Moves with model but is fixed, not learned by optimizer.

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Add the first seq_len positional vectors to x of shape [batch,seq_len,d_model]."""
        seq_len = x.size(1)  # Sequence dimension is axis 1.
        return x + self.pe[:, :seq_len, :]  # Slice to current length; broadcasting handles batch.


class MultiHeadAttention(nn.Module):
    """Project queries/keys/values, attend in parallel heads, then combine the heads."""
    def __init__(self, d_model: int, num_heads: int, dropout: float = 0.1):
        super().__init__()
        assert d_model % num_heads == 0, "d_model must be divisible by num_heads"
        self.d_model = d_model  # Total width of each token representation.
        self.num_heads = num_heads  # Number of parallel attention subspaces.
        self.d_k = d_model // num_heads  # Width assigned to each head.
        self.W_q = nn.Linear(d_model, d_model)  # Learn query vectors: what each token seeks.
        self.W_k = nn.Linear(d_model, d_model)  # Learn key vectors: what each token offers for matching.
        self.W_v = nn.Linear(d_model, d_model)  # Learn value vectors: information to aggregate.
        self.W_o = nn.Linear(d_model, d_model)  # Mix the joined output from all heads.
        self.dropout = nn.Dropout(dropout)  # Regularize attention probabilities during training.

    def scaled_dot_product_attention(self, Q, K, V, mask=None):
        """Calculate attention scores, mask forbidden positions, and combine values."""
        # Q=[B,H,Qlen,d_k], K=[B,H,Klen,d_k]; transpose K for [Qlen,Klen] scores.
        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.d_k)
        if mask is not None:  # Mask is broadcastable to [B,H,Qlen,Klen].
            scores = scores.masked_fill(mask == 0, -1e9)  # Huge negative score -> near-zero softmax weight.
        attn_probs = torch.softmax(scores, dim=-1)  # Turn scores for each query into weights summing to 1.
        attn_probs = self.dropout(attn_probs)  # Drop some weights during training for regularization.
        return torch.matmul(attn_probs, V)  # Weighted sum of values, one output per query and head.

    def forward(self, Q, K, V, mask=None):
        """Split projected vectors into heads, attend, join heads, and apply output projection."""
        batch_size = Q.size(0)
        # Project [B,length,d_model], reshape to [B,length,H,d_k], then move H before length.
        Q = self.W_q(Q).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)
        K = self.W_k(K).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)
        V = self.W_v(V).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)
        output = self.scaled_dot_product_attention(Q, K, V, mask)
        # Move length before heads, make memory contiguous, and merge H*d_k back into d_model.
        output = output.transpose(1, 2).contiguous().view(batch_size, -1, self.d_model)
        return self.W_o(output)  # Learned projection mixes the information from all heads.


class PositionwiseFeedForward(nn.Module):
    """Apply the same two-layer MLP separately to every token position."""
    def __init__(self, d_model: int, d_ff: int, dropout: float = 0.1):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(d_model, d_ff),  # Expand feature width.
            nn.ReLU(),  # Add non-linearity.
            nn.Dropout(dropout),  # Regularize hidden activations.
            nn.Linear(d_ff, d_model),  # Project back to model width.
        )

    def forward(self, x):
        """Transform the last feature dimension while preserving batch and sequence axes."""
        return self.net(x)


class EncoderLayer(nn.Module):
    """One encoder block: source self-attention, residual/normalization, then MLP."""
    def __init__(self, d_model: int, num_heads: int, d_ff: int, dropout: float):
        super().__init__()
        self.self_attn = MultiHeadAttention(d_model, num_heads, dropout)
        self.feed_forward = PositionwiseFeedForward(d_model, d_ff, dropout)
        self.norm1 = nn.LayerNorm(d_model)  # Stabilize features after attention residual.
        self.norm2 = nn.LayerNorm(d_model)  # Stabilize features after MLP residual.
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, src_mask):
        """Let every source token attend to source context, then refine each token with an MLP."""
        attn_output = self.self_attn(x, x, x, src_mask)  # Q=K=V=x means self-attention.
        x = self.norm1(x + self.dropout(attn_output))  # Residual add preserves prior representation.
        ff_output = self.feed_forward(x)
        x = self.norm2(x + self.dropout(ff_output))  # Second residual/normalization sublayer.
        return x


class DecoderLayer(nn.Module):
    """One decoder block: causal target attention, source cross-attention, then MLP."""
    def __init__(self, d_model: int, num_heads: int, d_ff: int, dropout: float):
        super().__init__()
        self.self_attn = MultiHeadAttention(d_model, num_heads, dropout)
        self.cross_attn = MultiHeadAttention(d_model, num_heads, dropout)
        self.feed_forward = PositionwiseFeedForward(d_model, d_ff, dropout)
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.norm3 = nn.LayerNorm(d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, enc_output, src_mask, trg_mask):
        """Use earlier English tokens and the encoded German sentence to update target vectors."""
        self_attn_output = self.self_attn(x, x, x, trg_mask)  # Causal mask blocks future English tokens.
        x = self.norm1(x + self.dropout(self_attn_output))
        # English queries attend to German keys/values to retrieve relevant source context.
        cross_attn_output = self.cross_attn(x, enc_output, enc_output, src_mask)
        x = self.norm2(x + self.dropout(cross_attn_output))
        ff_output = self.feed_forward(x)
        x = self.norm3(x + self.dropout(ff_output))
        return x


class Transformer(nn.Module):
    """Full German encoder and English autoregressive decoder."""
    def __init__(self, src_vocab_size: int, trg_vocab_size: int, src_pad_idx: int,
                 trg_pad_idx: int, d_model: int = 256, num_heads: int = 8,
                 num_layers: int = 3, d_ff: int = 512, max_seq_length: int = 100,
                 dropout: float = 0.1):
        super().__init__()
        self.src_pad_idx = src_pad_idx  # Source PAD ID used by source attention mask.
        self.trg_pad_idx = trg_pad_idx  # Target PAD ID used by target attention mask.
        self.d_model = d_model
        self.scale = math.sqrt(d_model)  # Scale embeddings before adding positional information.
        self.encoder_embedding = nn.Embedding(src_vocab_size, d_model)  # German ID -> learned vector.
        self.decoder_embedding = nn.Embedding(trg_vocab_size, d_model)  # English ID -> learned vector.
        # max_seq_length must cover the longest sentence; the demo uses 100 positions.
        self.positional_encoding = PositionalEncoding(d_model, max_seq_length)
        self.dropout = nn.Dropout(dropout)
        # ModuleList registers repeated layers so parameters are trained, saved, and moved to GPU.
        self.encoder_layers = nn.ModuleList([EncoderLayer(d_model, num_heads, d_ff, dropout)
                                             for _ in range(num_layers)])
        self.decoder_layers = nn.ModuleList([DecoderLayer(d_model, num_heads, d_ff, dropout)
                                             for _ in range(num_layers)])
        self.fc_out = nn.Linear(d_model, trg_vocab_size)  # Produce a score for each English word ID.

    def make_src_mask(self, src):
        """Mark non-PAD source tokens as visible to attention."""
        return (src != self.src_pad_idx).unsqueeze(1).unsqueeze(2)  # [B,1,1,src_len], broadcast over heads.

    def make_trg_mask(self, trg):
        """Hide target padding and future target positions (causal autoregressive mask)."""
        trg_pad_mask = (trg != self.trg_pad_idx).unsqueeze(1).unsqueeze(3)  # [B,1,trg_len,1].
        trg_len = trg.size(1)
        causal_mask = torch.tril(torch.ones((trg_len, trg_len), device=trg.device)).bool()
        return trg_pad_mask & causal_mask  # True only where target token is valid and not in the future.

    def encode(self, src, src_mask):
        """Embed German IDs, add positions, and pass through all encoder layers."""
        src_embedded = self.dropout(self.positional_encoding(self.encoder_embedding(src) * self.scale))
        enc_output = src_embedded
        for enc_layer in self.encoder_layers:
            enc_output = enc_layer(enc_output, src_mask)
        return enc_output  # Contextual source vectors consumed by decoder cross-attention.

    def decode(self, trg, enc_output, src_mask, trg_mask):
        """Embed English prefix IDs and pass through all decoder layers."""
        trg_embedded = self.dropout(self.positional_encoding(self.decoder_embedding(trg) * self.scale))
        dec_output = trg_embedded
        for dec_layer in self.decoder_layers:
            dec_output = dec_layer(dec_output, enc_output, src_mask, trg_mask)
        return dec_output

    def forward(self, src, trg):
        """Run masks, encoder, decoder, and output projection; return target-token logits."""
        src_mask = self.make_src_mask(src)
        trg_mask = self.make_trg_mask(trg)
        enc_output = self.encode(src, src_mask)
        dec_output = self.decode(trg, enc_output, src_mask, trg_mask)
        return self.fc_out(dec_output)  # [batch,target_len,target_vocab]; softmax is inside CrossEntropyLoss.


# ---------------------------------------------------------------------------
# Batching, optimization, evaluation, and translation
# ---------------------------------------------------------------------------

def make_collate_fn(src_vocab: Dict[str, int], trg_vocab: Dict[str, int]):
    """Return a DataLoader function that inserts boundaries, maps IDs, and pads a batch."""
    def collate_fn(batch):
        """Convert tokenized examples to two rectangular [batch,length] tensors."""
        src_batch, trg_batch = [], []
        for sample in batch:
            # Add SOS/EOS boundaries; .get uses UNK when a token is missing from the vocabulary.
            src_ids = [src_vocab.get(tok, src_vocab[UNK_TOKEN])
                       for tok in [SOS_TOKEN] + sample["src"] + [EOS_TOKEN]]
            trg_ids = [trg_vocab.get(tok, trg_vocab[UNK_TOKEN])
                       for tok in [SOS_TOKEN] + sample["trg"] + [EOS_TOKEN]]
            src_batch.append(torch.tensor(src_ids, dtype=torch.long))  # Embedding indices are integers.
            trg_batch.append(torch.tensor(trg_ids, dtype=torch.long))
        src_batch = pad_sequence(src_batch, padding_value=src_vocab[PAD_TOKEN], batch_first=True)
        trg_batch = pad_sequence(trg_batch, padding_value=trg_vocab[PAD_TOKEN], batch_first=True)
        return src_batch, trg_batch
    return collate_fn  # Nested function remembers the vocabulary dictionaries (closure).


def train_epoch(model, iterator, optimizer, criterion, clip: float) -> float:
    """Train over all batches once; return the mean batch loss."""
    model.train()  # Enables dropout and other training behavior.
    epoch_loss = 0.0
    for src, trg in tqdm(iterator, desc="Training", leave=False):
        src = src.to(device)  # Move source data to match model's CPU/GPU device.
        trg = trg.to(device)  # All tensors in a model operation must share the same device.
        optimizer.zero_grad()  # Clear previous batch gradients.
        output = model(src, trg[:, :-1])  # Teacher forcing: input target without EOS to predict next tokens.
        output_dim = output.shape[-1]  # Target vocabulary size.
        output = output.contiguous().view(-1, output_dim)  # Flatten batch and positions for cross entropy.
        target = trg[:, 1:].contiguous().view(-1)  # Shift labels left: omit SOS, predict following token.
        loss = criterion(output, target)  # PAD labels are ignored by the configured criterion.
        loss.backward()  # Compute gradients through the model.
        torch.nn.utils.clip_grad_norm_(model.parameters(), clip)  # Prevent excessively large gradients.
        optimizer.step()  # Update learned parameters.
        epoch_loss += loss.item()  # Add this batch's scalar loss to the epoch total.
    return epoch_loss / len(iterator)  # Mean loss per batch for easy reporting.


def evaluate(model, iterator, criterion) -> float:
    """Compute validation loss without updating model weights or retaining gradients."""
    model.eval()  # Turns dropout off.
    epoch_loss = 0.0
    with torch.no_grad():  # Save compute and memory because gradients are not needed for evaluation.
        for src, trg in tqdm(iterator, desc="Evaluating", leave=False):
            src = src.to(device)
            trg = trg.to(device)
            output = model(src, trg[:, :-1])
            output_dim = output.shape[-1]
            output = output.contiguous().view(-1, output_dim)
            target = trg[:, 1:].contiguous().view(-1)
            loss = criterion(output, target)
            epoch_loss += loss.item()
    return epoch_loss / len(iterator)  # Validation metric; optimizer is never called here.


def epoch_time(start_time: float, end_time: float) -> Tuple[int, int]:
    """Convert start/end timestamps into integer minutes and remaining seconds."""
    elapsed = end_time - start_time
    mins = int(elapsed / 60)
    secs = int(elapsed - (mins * 60))
    return mins, secs


def translate_sentence(sentence: str, src_vocab: Dict[str, int], trg_vocab: Dict[str, int],
                       model: Transformer, max_len: int = 50) -> List[str]:
    """Greedily translate German: repeatedly append the highest-scoring English token."""
    model.eval()  # Disable dropout during inference.
    idx_to_trg = {idx: token for token, idx in trg_vocab.items()}  # Reverse ID lookup for output words.
    tokens = [SOS_TOKEN] + tokenize_de(sentence) + [EOS_TOKEN]
    src_indexes = [src_vocab.get(token, src_vocab[UNK_TOKEN]) for token in tokens]
    src_tensor = torch.tensor(src_indexes, dtype=torch.long, device=device).unsqueeze(0)
    # The unsqueeze adds batch size 1; tensor is created directly on the model's device.
    src_mask = model.make_src_mask(src_tensor)
    with torch.no_grad():
        enc_output = model.encode(src_tensor, src_mask)  # Encode source once, before word generation.
    trg_indexes = [trg_vocab[SOS_TOKEN]]  # Begin target with start-of-sentence ID.
    for _ in range(max_len):  # Stop after max_len even if model never emits EOS.
        trg_tensor = torch.tensor(trg_indexes, dtype=torch.long, device=device).unsqueeze(0)
        trg_mask = model.make_trg_mask(trg_tensor)  # Causal mask for the current generated prefix.
        with torch.no_grad():
            dec_output = model.decode(trg_tensor, enc_output, src_mask, trg_mask)
            output = model.fc_out(dec_output)  # Scores for all English words at every prefix position.
        pred_token = output.argmax(dim=-1)[:, -1].item()  # Greedy choice at newest position.
        trg_indexes.append(pred_token)
        if pred_token == trg_vocab[EOS_TOKEN]:  # EOS is the model's signal that translation is finished.
            break
    trg_tokens = [idx_to_trg.get(idx, UNK_TOKEN) for idx in trg_indexes]
    return trg_tokens[1:-1]  # Remove SOS and final EOS/boundary token, as in the notebook.


# ---------------------------------------------------------------------------
# Main training flow (the notebook ran this directly in its last cell)
# ---------------------------------------------------------------------------

def main() -> None:
    """Load data, create model, train/validate, save best weights, then show translations."""
    if DOWNLOAD_DATASET:  # Optional replacement for the notebook's six wget commands.
        download_multi30k()
    train_data, val_data, test_data, SRC_VOCAB, TRG_VOCAB = build_datasets_and_vocabs()
    print("Source vocab size:", len(SRC_VOCAB))
    print("Target vocab size:", len(TRG_VOCAB))

    # Demo hyperparameters; the notebook trains for just one epoch for demonstration.
    D_MODEL = 256  # Feature width of token embeddings and attention vectors.
    NUM_HEADS = 8  # Parallel heads; must divide D_MODEL evenly.
    NUM_LAYERS = 3  # Number of encoder blocks and decoder blocks.
    D_FF = 512  # Hidden width of each feed-forward network.
    MAX_SEQ_LENGTH = 100  # Positional encoding capacity; longer inputs need a larger value.
    DROPOUT = 0.1  # Fraction of selected activations dropped during training.

    model = Transformer(
        src_vocab_size=len(SRC_VOCAB),  # Number of German embedding rows.
        trg_vocab_size=len(TRG_VOCAB),  # Number of English embedding rows/output classes.
        src_pad_idx=SRC_VOCAB[PAD_TOKEN],  # Used to create source attention masks.
        trg_pad_idx=TRG_VOCAB[PAD_TOKEN],  # Used to create target attention masks.
        d_model=D_MODEL, num_heads=NUM_HEADS, num_layers=NUM_LAYERS,
        d_ff=D_FF, max_seq_length=MAX_SEQ_LENGTH, dropout=DROPOUT,
    ).to(device)  # Move model parameters and positional buffer onto selected device.
    print(f"The model has {sum(p.numel() for p in model.parameters() if p.requires_grad):,} trainable parameters")

    optimizer = optim.Adam(model.parameters(), lr=1e-4, betas=(0.9, 0.98), eps=1e-9)
    # Adam changes parameters based on gradients; lr is learning rate, betas/eps tune its updates.
    criterion = nn.CrossEntropyLoss(ignore_index=TRG_VOCAB[PAD_TOKEN])
    # Cross entropy trains next-token prediction; ignore PAD labels so padding does not affect loss.
    BATCH_SIZE = 32  # Number of paired sentences in a batch.
    N_EPOCHS = 1  # The original demo setting; better translations need more training.
    CLIP = 1.0  # Maximum gradient norm used in train_epoch.

    collate_fn = make_collate_fn(SRC_VOCAB, TRG_VOCAB)
    train_loader = DataLoader(train_data, batch_size=BATCH_SIZE, shuffle=True, collate_fn=collate_fn)
    val_loader = DataLoader(val_data, batch_size=BATCH_SIZE, shuffle=False, collate_fn=collate_fn)
    best_valid_loss = float("inf")  # Any finite first validation loss is an improvement.
    # Use a new checkpoint filename so this companion never overwrites the notebook's existing file.
    checkpoint_path = SCRIPT_DIR / "transformer-translation-model-explained.pt"

    for epoch in range(N_EPOCHS):
        start = time.time()
        train_loss = train_epoch(model, train_loader, optimizer, criterion, CLIP)
        valid_loss = evaluate(model, val_loader, criterion)
        end = time.time()
        mins, secs = epoch_time(start, end)
        if valid_loss < best_valid_loss:  # Keep the weights that perform best on validation data.
            best_valid_loss = valid_loss
            torch.save(model.state_dict(), checkpoint_path)  # Save parameter tensors to disk.
        print(f"Epoch: {epoch + 1:02} | Time: {mins}m {secs}s")
        print(f"\tTrain Loss: {train_loss:.3f} | Train PPL: {math.exp(train_loss):7.3f}")
        print(f"\t Val. Loss: {valid_loss:.3f} |  Val. PPL: {math.exp(valid_loss):7.3f}")
        # PPL/perplexity is exp(loss), a measure of how surprised the model is by correct next tokens.

    model.load_state_dict(torch.load(checkpoint_path, map_location=device))  # Reload best weights.
    print("\nExample translations:\n")
    for example_idx in range(min(3, len(test_data))):  # Print up to three test examples.
        src = test_data[example_idx]["src"]  # German input tokens.
        trg = test_data[example_idx]["trg"]  # Human English reference tokens.
        pred = translate_sentence(" ".join(src), SRC_VOCAB, TRG_VOCAB, model)
        print("Source:   ", " ".join(src))
        print("Target:   ", " ".join(trg))
        print("Predicted:", " ".join(pred))
        print()  # Blank separator between examples.


# Importing this file defines functions/classes but does not launch training.
# Run it directly with Python to execute main(). Ensure the dataset files are in data/.
if __name__ == "__main__":
    main()
