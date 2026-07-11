import time
import subprocess
import os
import sys

# Wait for login
timeout = 30
start_time = time.time()
user = "Guest"

while not os.path.exists("username.txt"):
    if time.time() - start_time > timeout:
        print("Timeout waiting for login!")
        break
    time.sleep(1)
else:
    with open("username.txt", "r") as f:
        user = f.read().strip()

# Main shell loop
while True:
    try:
        parts = input(f"{user}@TrashOS~ ").strip().split(maxsplit=1)
        if not parts: continue
        cmd, arg = parts[0], parts[1] if len(parts) > 1 else ""

        if cmd == "help":
            with open("help.txt", "r") as y: print(y.read())
        elif cmd == "trashfetch": subprocess.run(['python', 'trashfetch.py'])
        elif cmd == "calc": subprocess.run(['python', 'calculator.py'])
        elif cmd == "echo": subprocess.run(['python', 'echo.py', arg])
        elif cmd == "ping": subprocess.run(['python', 'pingip.py'])
        elif cmd == "matrix": subprocess.run(['python', 'matrix.py'])
        elif cmd == "clear": os.system('cls' if os.name == 'nt' else 'clear')
        elif cmd == "exit": sys.exit(0)
        else: print(f"Command {cmd} not found, perhaps you spelled it wrong?")
    except KeyboardInterrupt:
        print("Use command exit to exit")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Report to TrashOS Repo issues")
    except EOFError:
        print("Use command exit to exit")
    