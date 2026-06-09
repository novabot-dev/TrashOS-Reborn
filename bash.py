import time
import subprocess
import os

# Wait for username.txt to be created (with timeout)
timeout = 30  # seconds
start_time = time.time()

while not os.path.exists("username.txt"):
    if time.time() - start_time > timeout:
        print("Timeout waiting for login!")
        user = "Guest"
        break
    print("Waiting for login to complete...")
    time.sleep(1)
else:
    with open("username.txt", "r") as f:
        user = f.read().strip()

while True:
    prompt = f"{user}@TrashOS~ "
    cmd = input(prompt)
    if cmd == "help":
        with open("help.txt", "r") as y:
            help = y.read()
        print(help)
    elif cmd == "trashfetch":
        subprocess.run(['python', 'trashfetch.py'])
    elif cmd == "calc":
        subprocess.run(['python', 'calculator.py'])
    else:
        print(f"Command {cmd} not found, perhaps you spelled it wrong?")