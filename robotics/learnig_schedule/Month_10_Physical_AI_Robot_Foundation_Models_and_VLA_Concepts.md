# Robotics & Physical AI — Month 10: Physical AI, Robot Foundation Models and VLA Concepts

**Course length:** 12-month programme, 52 weeks; 676–910 planned study hours at 13–17.5 hours/week  
**Learner profile:** 10+ years embedded software engineering; STM32/ESP32, RTOS, C/C++, Python, CAN/serial; current GenAI/LLM/RAG/MCP exposure  
**Primary method:** derive → implement → test → simulate → integrate → explain  
**Month gate:** earn at least 70/100 and complete all mandatory practical evidence before moving on. A score below 70 means targeted remediation, not simply re-reading.

**Official program start:** Sunday, 2026-11-15 (Asia/Kolkata). Complete the Month 1 kickoff and baseline on that Sunday; start its Week 01 Monday task on 2026-11-16. Follow the month files in sequence and use the progress tracker to identify the current month and week.

## How to use this file
1. Read the monthly outcomes and establish a baseline.
2. Work through every weekly plan and daily task. Commit code in small increments.
3. On Sunday, take the written exam without notes, answer interview prompts aloud, and update the learning notebook.
4. At month end, submit the project, exam, evidence and self-review for mentor review.

## Study-time contract (13–17.5 hours/week)
- Monday–Friday: 1–1.5 hours/day (5–7.5 hours total).
- Saturday: 4–5 hours (deep lab/integration block).
- Sunday: 4–5 hours (review, written test, interview practice and notes).
- Each weekday block: 15–20 min reading, 10–15 min derivation/notes, 35–60 min coding or lab, and 5 min log/commit; choose the shorter version on a 1-hour day.
- Saturday: 30 min planning, 2.5–3.5 hours building/testing, 45–60 min debugging, and 15–30 min demo/log.
- Sunday: 45–60 min written check, 20–30 min interview practice, 60–90 min revision, and 30–45 min weekly report/next-week plan; use remaining time for the assigned practical.

If a workday is missed, do not silently compress the learning objectives. Move the missed lab into the next Saturday buffer and record the slip in the progress log.

## Monthly outcomes
By the end of Month 10, you should be able to explain, implement and defend the following: 
- Primary focus: **Physical AI, Robot Foundation Models and VLA Concepts**.
- Explain the underlying theory and mathematical assumptions, not just API usage.
- Implement the core algorithm or software pattern in a version-controlled repository.
- Integrate the topic into a ROS 2 node/interface or a well-defined ROS 2-facing adapter.
- Reproduce the result in simulation and evaluate it with metrics.
- Describe one industry use case, one failure mode and one safety/reliability measure.
- Planned effort: **4 weeks × 13–17.5 h = 52–70 hours**.

## Prerequisite and setup checklist
- [ ] Ubuntu/Linux development environment is documented; use a version-compatible ROS 2 distribution and simulator pairing.
- [ ] Python virtual environment and dependency lock/requirements are committed.
- [ ] Git repository created with README, license decision, .gitignore, tests and issue tracker.
- [ ] Use a single chosen ROS 2 distribution for the main workspace. Confirm package compatibility before adding simulators or GPU tools.
- [ ] Safety rule: learned/high-level outputs must never directly drive physical actuators without a deterministic validation, limits, watchdog and emergency-stop layer.

## Core theory explained through worked examples

- **VLA pipeline:** Image + language + proprioception → multimodal model → action representation → safety filter → robot controller. Identify every trust boundary.
- **Action tokenization:** Quantize a 1D action in [−1,1] into 256 bins. Calculate resolution and maximum quantization error.
- **Model comparison:** Compare RT-1, RT-2, OpenVLA and GR00T by training data, embodiment, action format, release artifacts, inference needs and evaluation evidence.

## Weekly training blocks
## Week 40 — Embodied intelligence and VLA architecture
**Expected outcome:** Explain the perception-language-action loop and its limits.
**Theory syllabus:** VLM vs VLA; embodiment; action tokens; closed-loop control; grounding; latency; dataset dependence.
**Mathematical foundation:** Derive the equations relevant to Embodied intelligence and VLA architecture; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Build an illustrative VLA I/O pipeline using a frozen vision-language model or mock action tokenizer.
**ROS 2 implementation:** Define a ROS 2 action schema and safety-bounded executor; keep language model output non-executable until validated.
**Simulation exercise:** Simulate a language-conditioned object selection task with deterministic low-level control.
**Practical assignment:** Draw and explain end-to-end VLA and hierarchical VLM+planner+controller architectures.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Embodied intelligence and VLA architecture**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: VLM vs VLA.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Embodied intelligence and VLA architecture; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Build an illustrative VLA I/O pipeline using a frozen vision-language model or mock action tokenizer.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Define a ROS 2 action schema and safety-bounded executor; keep language model output non-executable until validated.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Simulate a language-conditioned object selection task with deterministic low-level control.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Draw and explain end-to-end VLA and hierarchical VLM+planner+controller architectures.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [OpenVLA project and implementation](https://github.com/openvla/openvla)
- [OpenVLA paper](https://arxiv.org/abs/2406.09246)
- [RT-1: Robotics Transformer for real-world control at scale](https://research.google/blog/rt-1-robotics-transformer-for-real-world-control-at-scale/)
- [RT-2 paper](https://arxiv.org/abs/2307.15818)
- [NVIDIA GR00T developer resources](https://developer.nvidia.com/isaac/gr00t)
- [NVIDIA GR00T technical blog](https://developer.nvidia.com/blog/develop-humanoid-robot-policies-end-to-end-with-nvidia-isaac-gr00t/)
- [YouTube — vision-language-action models for robotics](https://www.youtube.com/results?search_query=vision+language+action+models+robotics+OpenVLA+RT2+lecture)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Embodied intelligence and VLA architecture** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Embodied intelligence and VLA architecture; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Embodied intelligence and VLA architecture** to a robotics engineer who has not used this technique.
2. What assumptions are hidden in your implementation of this week’s exercise?
3. How would you test the solution on a robot rather than only in a notebook?
4. Describe one bug you encountered or anticipate. How would you isolate it?
5. What metric would you use to decide whether your result is good enough?
6. How does this concept connect to your embedded background (timing, sensors, RTOS, interfaces, safety or fault handling)?

### Weekly pass criteria
- [ ] Written exam score ≥ 14/20 (70%).
- [ ] Coding artifact runs from a clean checkout and has at least 3 meaningful tests.
- [ ] ROS 2 or interface mock is demonstrated with evidence (terminal capture, bag, test or launch log).
- [ ] Simulation result is saved with configuration and at least one edge case.
- [ ] Interview answers are recorded; at least 4/6 are clear, technically correct and evidence-backed.
- [ ] Weekly notes and Git commit/pull request are complete.

### Weekly reviewer feedback
**Score:** ___ / 20 written | ___ / 10 practical | ___ / 10 explanation  
**Strongest evidence:**  
**Misconception / gap:**  
**Corrective assignment:**  
**Reviewer decision:** Pass / Revise / Re-test  

## Week 41 — RT-1 and RT-2 research analysis
**Expected outcome:** Compare robot transformer design choices and evidence.
**Theory syllabus:** tokenization; action discretization; data scale; co-training; generalization; closed-loop control; limitations.
**Mathematical foundation:** Derive the equations relevant to RT-1 and RT-2 research analysis; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Implement a tiny action-token discretizer and decoder for a toy robot state/action space.
**ROS 2 implementation:** Convert decoded actions into typed, bounded ROS 2 command messages in simulation only.
**Simulation exercise:** Test action quantization error on a simple end-effector trajectory.
**Practical assignment:** Prepare a 2-page critical paper review distinguishing claim, evidence and limitation.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **RT-1 and RT-2 research analysis**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: tokenization.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to RT-1 and RT-2 research analysis; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Implement a tiny action-token discretizer and decoder for a toy robot state/action space.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Convert decoded actions into typed, bounded ROS 2 command messages in simulation only.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Test action quantization error on a simple end-effector trajectory.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Prepare a 2-page critical paper review distinguishing claim, evidence and limitation.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [OpenVLA project and implementation](https://github.com/openvla/openvla)
- [OpenVLA paper](https://arxiv.org/abs/2406.09246)
- [RT-1: Robotics Transformer for real-world control at scale](https://research.google/blog/rt-1-robotics-transformer-for-real-world-control-at-scale/)
- [RT-2 paper](https://arxiv.org/abs/2307.15818)
- [NVIDIA GR00T developer resources](https://developer.nvidia.com/isaac/gr00t)
- [NVIDIA GR00T technical blog](https://developer.nvidia.com/blog/develop-humanoid-robot-policies-end-to-end-with-nvidia-isaac-gr00t/)
- [YouTube — vision-language-action models for robotics](https://www.youtube.com/results?search_query=vision+language+action+models+robotics+OpenVLA+RT2+lecture)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **RT-1 and RT-2 research analysis** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to RT-1 and RT-2 research analysis; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **RT-1 and RT-2 research analysis** to a robotics engineer who has not used this technique.
2. What assumptions are hidden in your implementation of this week’s exercise?
3. How would you test the solution on a robot rather than only in a notebook?
4. Describe one bug you encountered or anticipate. How would you isolate it?
5. What metric would you use to decide whether your result is good enough?
6. How does this concept connect to your embedded background (timing, sensors, RTOS, interfaces, safety or fault handling)?

### Weekly pass criteria
- [ ] Written exam score ≥ 14/20 (70%).
- [ ] Coding artifact runs from a clean checkout and has at least 3 meaningful tests.
- [ ] ROS 2 or interface mock is demonstrated with evidence (terminal capture, bag, test or launch log).
- [ ] Simulation result is saved with configuration and at least one edge case.
- [ ] Interview answers are recorded; at least 4/6 are clear, technically correct and evidence-backed.
- [ ] Weekly notes and Git commit/pull request are complete.

### Weekly reviewer feedback
**Score:** ___ / 20 written | ___ / 10 practical | ___ / 10 explanation  
**Strongest evidence:**  
**Misconception / gap:**  
**Corrective assignment:**  
**Reviewer decision:** Pass / Revise / Re-test  

## Week 42 — OpenVLA codebase and inference workflow
**Expected outcome:** Understand a public VLA implementation and its deployment constraints.
**Theory syllabus:** vision-language backbone; action head; proprioception; normalization; inference; checkpoint/license; hardware needs.
**Mathematical foundation:** Derive the equations relevant to OpenVLA codebase and inference workflow; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Set up repository in a separate environment; inspect configs; run available inference/demo only if compute permits.
**ROS 2 implementation:** Create a mock observation/action adapter with schema validation and command-rate limits.
**Simulation exercise:** Evaluate a pretrained or small mock policy using an offline benchmark; avoid direct unguarded actuation.
**Practical assignment:** Report GPU memory, latency, dependencies and failure modes.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **OpenVLA codebase and inference workflow**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: vision-language backbone.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to OpenVLA codebase and inference workflow; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Set up repository in a separate environment; inspect configs; run available inference/demo only if compute permits.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Create a mock observation/action adapter with schema validation and command-rate limits.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Evaluate a pretrained or small mock policy using an offline benchmark; avoid direct unguarded actuation.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Report GPU memory, latency, dependencies and failure modes.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [OpenVLA project and implementation](https://github.com/openvla/openvla)
- [OpenVLA paper](https://arxiv.org/abs/2406.09246)
- [RT-1: Robotics Transformer for real-world control at scale](https://research.google/blog/rt-1-robotics-transformer-for-real-world-control-at-scale/)
- [RT-2 paper](https://arxiv.org/abs/2307.15818)
- [NVIDIA GR00T developer resources](https://developer.nvidia.com/isaac/gr00t)
- [NVIDIA GR00T technical blog](https://developer.nvidia.com/blog/develop-humanoid-robot-policies-end-to-end-with-nvidia-isaac-gr00t/)
- [YouTube — vision-language-action models for robotics](https://www.youtube.com/results?search_query=vision+language+action+models+robotics+OpenVLA+RT2+lecture)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **OpenVLA codebase and inference workflow** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to OpenVLA codebase and inference workflow; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **OpenVLA codebase and inference workflow** to a robotics engineer who has not used this technique.
2. What assumptions are hidden in your implementation of this week’s exercise?
3. How would you test the solution on a robot rather than only in a notebook?
4. Describe one bug you encountered or anticipate. How would you isolate it?
5. What metric would you use to decide whether your result is good enough?
6. How does this concept connect to your embedded background (timing, sensors, RTOS, interfaces, safety or fault handling)?

### Weekly pass criteria
- [ ] Written exam score ≥ 14/20 (70%).
- [ ] Coding artifact runs from a clean checkout and has at least 3 meaningful tests.
- [ ] ROS 2 or interface mock is demonstrated with evidence (terminal capture, bag, test or launch log).
- [ ] Simulation result is saved with configuration and at least one edge case.
- [ ] Interview answers are recorded; at least 4/6 are clear, technically correct and evidence-backed.
- [ ] Weekly notes and Git commit/pull request are complete.

### Weekly reviewer feedback
**Score:** ___ / 20 written | ___ / 10 practical | ___ / 10 explanation  
**Strongest evidence:**  
**Misconception / gap:**  
**Corrective assignment:**  
**Reviewer decision:** Pass / Revise / Re-test  

## Week 43 — GR00T and humanoid foundation model ecosystem
**Expected outcome:** Understand humanoid data pipelines and generalist policy training.
**Theory syllabus:** humanoid embodiment; teleoperation; synthetic + real data; action representation; whole-body control; evaluation.
**Mathematical foundation:** Derive the equations relevant to GR00T and humanoid foundation model ecosystem; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Build a dataset manifest and action normalization demo for multi-joint trajectories.
**ROS 2 implementation:** Map high-level skill requests to typed skill/action interfaces with a safety gate.
**Simulation exercise:** Inspect official GR00T/Isaac learning examples that match available release and hardware.
**Practical assignment:** Write a comparison matrix: RT-1, RT-2, OpenVLA and GR00T—scope, data, action, compute, limits.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **GR00T and humanoid foundation model ecosystem**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: humanoid embodiment.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to GR00T and humanoid foundation model ecosystem; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Build a dataset manifest and action normalization demo for multi-joint trajectories.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Map high-level skill requests to typed skill/action interfaces with a safety gate.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Inspect official GR00T/Isaac learning examples that match available release and hardware.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Write a comparison matrix: RT-1, RT-2, OpenVLA and GR00T—scope, data, action, compute, limits.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [OpenVLA project and implementation](https://github.com/openvla/openvla)
- [OpenVLA paper](https://arxiv.org/abs/2406.09246)
- [RT-1: Robotics Transformer for real-world control at scale](https://research.google/blog/rt-1-robotics-transformer-for-real-world-control-at-scale/)
- [RT-2 paper](https://arxiv.org/abs/2307.15818)
- [NVIDIA GR00T developer resources](https://developer.nvidia.com/isaac/gr00t)
- [NVIDIA GR00T technical blog](https://developer.nvidia.com/blog/develop-humanoid-robot-policies-end-to-end-with-nvidia-isaac-gr00t/)
- [YouTube — vision-language-action models for robotics](https://www.youtube.com/results?search_query=vision+language+action+models+robotics+OpenVLA+RT2+lecture)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **GR00T and humanoid foundation model ecosystem** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to GR00T and humanoid foundation model ecosystem; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **GR00T and humanoid foundation model ecosystem** to a robotics engineer who has not used this technique.
2. What assumptions are hidden in your implementation of this week’s exercise?
3. How would you test the solution on a robot rather than only in a notebook?
4. Describe one bug you encountered or anticipate. How would you isolate it?
5. What metric would you use to decide whether your result is good enough?
6. How does this concept connect to your embedded background (timing, sensors, RTOS, interfaces, safety or fault handling)?

### Weekly pass criteria
- [ ] Written exam score ≥ 14/20 (70%).
- [ ] Coding artifact runs from a clean checkout and has at least 3 meaningful tests.
- [ ] ROS 2 or interface mock is demonstrated with evidence (terminal capture, bag, test or launch log).
- [ ] Simulation result is saved with configuration and at least one edge case.
- [ ] Interview answers are recorded; at least 4/6 are clear, technically correct and evidence-backed.
- [ ] Weekly notes and Git commit/pull request are complete.

### Weekly reviewer feedback
**Score:** ___ / 20 written | ___ / 10 practical | ___ / 10 explanation  
**Strongest evidence:**  
**Misconception / gap:**  
**Corrective assignment:**  
**Reviewer decision:** Pass / Revise / Re-test  

## Month-end practical project
**Project objective:** Build a portfolio-quality artifact that integrates the month’s central concepts and can be reproduced by another engineer.
**Project name:** Vision-language-action research and safe action adapter**
### Minimum acceptance criteria
- [ ] A clear problem statement, requirements and system/block diagram.
- [ ] A mathematical or algorithmic explanation with one worked example.
- [ ] Source code organized into modules; meaningful names, comments and tests.
- [ ] A reproducible setup, configuration and run command.
- [ ] Simulation or offline evaluation with a baseline and at least 3 metrics.
- [ ] Failure analysis: at least 3 failure modes and mitigations.
- [ ] Demo video or terminal walkthrough and 1–3 page engineering report.
- [ ] GitHub README, diagram, dependencies and known limitations.

## Month-end written examination (100 minutes; 40 points)
1. Explain the month’s central system/algorithm from first principles (8 points).
2. Solve a numerical or derivation problem from the worked examples (8 points).
3. Analyze a code/configuration snippet: identify the defect, edge case or performance issue (6 points).
4. Design a practical system block diagram with interfaces, data types, timing and error handling (6 points).
5. Analyze a failure scenario and propose a testable correction (6 points).
6. Write an engineering summary of your project results, including metrics and limitations (6 points).
**Pass:** 28/40 (70%), with no critical safety misconception.

### Month-specific written exam questions

1. Draw and explain VLM, VLA and hierarchical VLM-planner-controller architectures.
2. Describe RT-1’s input/action representation and the role of large-scale robot data.
3. Explain RT-2’s central idea of co-fine-tuning vision-language models with robot trajectories.
4. Quantize a continuous action interval into 256 bins and calculate quantization resolution.
5. Summarize OpenVLA’s model/task scope and its training/evaluation resources.
6. Compare GR00T’s focus and workflow with general-purpose VLA manipulation models.
7. Identify latency and control-rate constraints in closing the loop with a foundation model.
8. Design a safe action-validation boundary between model output and ROS 2 control.

### Month-specific interview questions

1. What distinguishes a VLA from a VLM?
2. Why is robot action representation a central design choice?
3. What did RT-1 demonstrate and what were its data requirements?
4. What knowledge transfer is RT-2 attempting to enable?
5. What would you inspect first when reproducing OpenVLA inference?
6. Why should a foundation model not publish arbitrary actuator commands?
7. How do you evaluate generalization to unseen objects and instructions?
8. What evidence would convince you that a VLA works beyond a curated demo?

## Month-end interview question bank
1. Explain **Physical AI, Robot Foundation Models and VLA Concepts** as though you are in a technical interview.
2. Which assumptions in your project are most likely to fail on a real robot?
3. Explain one equation/algorithm you used and derive it at a high level.
4. What measurements prove your implementation works? What would falsify your claim?
5. What is the most important trade-off you made and what alternative did you reject?
6. How do you handle invalid input, timeouts, stale data and component failure?
7. How would you make the system deterministic and reproducible enough for regression testing?
8. What would you change for a production deployment with safety and uptime requirements?
9. Explain one relevant research paper: problem, method, result, limitation and practical lesson.
10. What did you build independently, what did you adapt, and how can another engineer reproduce it?

## Evaluation rubric (100 points)
| Area | Points | Evidence required |
|---|---:|---|
| Theory and mathematical reasoning | 20 | Correct explanation, derivation, assumptions and units |
| Coding quality | 15 | Readable implementation, tests, reproducible environment |
| ROS 2/software integration | 15 | Correct interfaces, launch/config, timing and observability |
| Simulation / experiment quality | 15 | Repeatable trials, baseline and meaningful metrics |
| Practical project outcome | 15 | Functional demonstration and requirements traceability |
| Written exam | 10 | Clear, accurate, structured responses |
| Interview / communication | 5 | Concise explanation and sound trade-offs |
| Notes and engineering discipline | 5 | Complete lab logs, paper notes and weekly retrospective |

### Readiness interpretation
- **90–100: Strong:** can implement and defend the topic with minimal guidance.
- **80–89: Ready:** solid practical ability; a few gaps need targeted practice.
- **70–79: Conditional:** proceed with a remediation ticket and revisit weak concepts.
- **Below 70: Not ready:** repeat the weak week(s), re-test and do not hide gaps behind attendance.
- **Automatic review required:** unsafe actuator behavior, incorrect coordinate-frame assumptions, invalid evaluation methodology or inability to reproduce the result.

## Learning progress tracker
| Week | Planned hours | Actual hours | Written /20 | Practical /10 | Interview /10 | Evidence link | Status |
|---|---:|---:|---:|---:|---:|---|---|
| 40 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 41 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 42 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 43 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |

**Month total:** Planned ___ / 76 hours | Actual ___ hours | Month score ___ / 100 | Decision: Pass / Conditional / Repeat

## Notes to capture this month
For every training day, use the matching template in `../Robotics_Physical_AI_Learner_Notebook.md`. Do not rely on memory: capture equations, units, assumptions, code experiments, ROS graph, simulator configuration, screenshots/links, bugs and corrections.

### Month-end reflection
- What can I now explain without notes?
- What can I implement from a blank file?
- Which result did I validate against a known answer or baseline?
- Which three mistakes taught me the most?
- What remains weak, and what exact exercise will close the gap?
- What evidence should a hiring manager inspect first?
