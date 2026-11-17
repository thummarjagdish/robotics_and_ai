import time
from wakepy import keep

# Keeps both the system and the display awake
with keep.presenting():
    print("Laptop will stay awake. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        print("Stopped. Normal sleep settings restored.")