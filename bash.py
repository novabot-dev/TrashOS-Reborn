import time
import subprocess
import os
import sys
import difflib
import json
from pathlib import Path
SAFE_MODE = ""
APPS_DIR = Path(__file__).resolve().parent / "tosapps"
STATUS_API_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tosapi_status.json")


def sync_tosapi_status():
    payload = {
        "version": "1.1.1",
        "is_root": user == "root"
    }
    with open(STATUS_API_FILE, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=4)

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
    sync_tosapi_status()

# Main shell loop
while True:
    try:
        parts = input(f"{user}@TrashOS~ ").strip().split(maxsplit=1)
        if not parts: continue
        cmd = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else ""

        if cmd == "help":
            with open("help.txt", "r") as y: print(y.read())
        elif cmd == "trashfetch": subprocess.run(['python', 'trashfetch.py'])
        elif cmd == "calc": subprocess.run(['python', 'calculator.py'])
        elif cmd == "echo": subprocess.run(['python', 'echo.py', arg])
        elif cmd == "ping": subprocess.run(['python', 'pingip.py'])
        elif cmd == "matrix": subprocess.run(['python', 'matrix.py'])
        elif cmd == "clear": os.system('cls' if os.name == 'nt' else 'clear')
        elif cmd in {"root", "sudo"}:
            if user == "root":
                print("Already running as root.")
            else:
                password = input("Password for root: ").strip()
                if password == "root":
                    user = "root"
                    sync_tosapi_status()
                    print("Root access granted.")
                else:
                    print("Incorrect root password.")
        elif cmd == "restart" or cmd == "reboot":
            print("Restarting TrashOS...")
            time.sleep(1)
            subprocess.run([sys.executable, 'kernel.py'])
            exit(0)
        elif cmd == "shutdown":
            print("Shutting down TrashOS...")
            time.sleep(1)
            exit(0)
        elif cmd == "reload":
            print("Reloading TrashOS...")
            time.sleep(1)
            subprocess.run([sys.executable, 'bash.py'])
            exit(0)
                    
        elif cmd == "exit": sys.exit(0)
        else:
            app_exec = os.path.join(APPS_DIR, f"{cmd}.py")
            if os.path.exists(app_exec):
                if SAFE_MODE:
                    print("App execution is disabled in Safe Mode.")
                else:
                    subprocess.run([sys.executable, app_exec])
            else:
                base_commands = "help","root","sudo","ver","browser","files", "calc", "shutdown", "hostos", "install", "changelog", "usrmgr", "ls", "mkdir", "clear", "rmdir", "touch", "rm", "ping", "matrix", "trashfetch", "restart", "exit"
                all_possibilities = list(base_commands)
                if not SAFE_MODE:
                    apps_in_folder = [f.replace(".py", "") for f in os.listdir(APPS_DIR)]
                    all_possibilities.extend(apps_in_folder)
                matches = difflib.get_close_matches(cmd, all_possibilities, n=1, cutoff=0.6)
                if matches:
                    print(f"Command {cmd} not found, Perhaps you meant the command \"{matches[0]}\"?")
                else:
                    print(f"Command {cmd} not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Report to TrashOS Repo issues")
    except EOFError:
        print("Use command exit to exit")