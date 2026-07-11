
import os
import random
import sys
import time
clear_def = lambda: os.system('cls' if os.name == 'nt' else 'clear')
print("Loading")
time.sleep(1)
try:
    while True:
        clear_def()
        chars = [random.choice(["0", "1", " ", " "]) for _ in range(40)]
        sys.stdout.write(" ".join(chars) + "\n")
        sys.stdout.flush()
        time.sleep(0.01)
except KeyboardInterrupt:
    print("\nClosed.")