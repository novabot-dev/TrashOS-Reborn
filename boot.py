import time
import sys
import json
import subprocess
import os
import webbrowser
import platform
import difflib
import shutil
from pathlib import Path

USERS_DB = "users.json"
log_user = "Pre-Boot"
is_root = False
root_passwd = "root"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
APPS_DIR = os.path.join(BASE_DIR, "tosapps")
host_os_type = platform.system()
host_os_release = platform.release()
host_os = f"{host_os_type} {host_os_release}"
base_commands = "help","root", "ver","browser","files", "calc", "shutdown", "hostos", "install", "echo", "apps", "changelog", "mkdir", "ls", "rmdir"
all_possibilities = list(base_commands)
apps_in_folder = [f.replace(".py", "") for f in os.listdir(APPS_DIR)]
all_possibilities.extend(apps_in_folder)
os_users = {
   "root": "root",
   "trash": "", 
   "sys": "",
}
if not os.path.exists(USERS_DB):
    json_users = os_users
    with open(USERS_DB, "w") as f:
        json.dump(os_users, f, indent=4)
else:
    with open(USERS_DB, "r") as f:
        os_users = json.load(f)



print("Booting system")
time.sleep(0.5)
print("POST success")

try:
    raw_cpu = subprocess.check_output("wmic cpu get name", shell=True)

    cpu_text_clean = raw_cpu.decode().splitlines()

    print("CPU:", cpu_text_clean[2].strip())

    raw_gpu_cmd = "wmic path Win32_VideoController get name"

    raw_result_gpu = subprocess.check_output(raw_gpu_cmd, shell=True)

    gpu_text_clean = raw_result_gpu.decode().splitlines()

    print("GPU:", gpu_text_clean[2].strip())
except:
    print("CPU: Generic processor")
    print("GPU: Generic software renderer")

time.sleep(2)
print("SGX disabled or unsupported by BIOS")
time.sleep(0.2)
print("Turning trosreb.bin into RAMDISK from BIN backup")
time.sleep(4)
print("TrashOS Reborn kernel loading")
time.sleep(8)
time.sleep(0.2)
time.sleep(0.2)
time.sleep(0.2)
print("Turned trosreb.bin into RAMDISK from BIN backup [OKAY]")
time.sleep(4)
time.sleep(8)
print("TrashOS Reborn Kernel loaded [OKAY]")
time.sleep(0.2)
print("Please report TrashOS Reborn issues to our GitHub")
print("placeholder_url")
time.sleep(0.2)
print("Logged in Pre-Boot user")
time.sleep(0.3)
print("Loading CPU feature set driver")
time.sleep(1.2)
print("Loaded CPU Driver [OKAY]")
time.sleep(1.2)
print("Loading full GPU driver")
time.sleep(1.2)
print("Loaded full GPU driver [OKAY]")
time.sleep(1.2)
print("Loading fan control driver")
time.sleep(1.2)
print("Loaded fan control driver [OKAY]")
time.sleep(1.2)
print("Loading bash")
time.sleep(2)
print("Loaded bash [OKAY]")
time.sleep(0.8)
print("Welcome to TrashOS 1.1.0!")
time.sleep(0.8)

while True:
    logged_in = False
    login_passwrd = ""
    while True:
        os_users_outp = ", ".join(os_users.keys())
        print(os_users_outp)
        login_usernm = input("Please enter username of user to log into: ")
        if login_usernm not in os_users:
            print("User not found!")
        else:
            login_passwrd = input ("Please enter password of user to log into: ")
        if login_usernm != "root":
            if login_usernm in os_users and os_users[login_usernm] == login_passwrd:
                print("Login success")
                log_user = login_usernm
                pass
                break
        else:
            if login_usernm in os_users:
                print("Password incorrect!")
        if logged_in == True:
            time.sleep(0.5)
            print(f"Welcome to TrashOS, {log_user}!!")
    
    def make_change_user():
        global log_user
        print(f"Type 1 to change user info of {log_user}")
        print(f"Type 2 to add user")
        print("Type 3 to exit")
        make_change_user_inp = input()

        if make_change_user_inp == "1":
            chng_pass = input("Type in your wanted password: ")
            chng_usr = input("Type in your wanted username: ")
            os_users.pop(log_user)
            os_users[chng_usr] = chng_pass
            log_user = chng_usr
            sync_usrdsk()
            print("Success!!")
            
        elif make_change_user_inp == "2":
            new_usrnm = input("Type in the wanted username for new user: ")
            time.sleep(0.2)
            new_passwd = input("Type in the wanted password for new user: ")
            os_users[new_usrnm] = new_passwd
            print("Success!!")
            sync_usrdsk()
        elif make_change_user_inp == "3":
            print("Exiting...")
            time.sleep(0.5)
            pass
        else:
            print("Invalid choice!") 


    def guess_game():
        import random
        number = random.randint(0,50)
        input_guess = int(input("Guess a number from 0-50:"))
        if input != number:
                print("Incorrect")
                print(f"The answer was {number}")
        else:
            print("correct")
    def sync_usrdsk():
        with open(USERS_DB, "w") as f:
            json.dump(os_users, f, indent=4)
    def mkdir_logic():
        mk_dirnam = input("mkdir: ")
        os.makedirs(mk_dirnam)
        ls_outp = os.listdir()
        ls_outclrmdir = ", ".join(os.listdir())
        print(ls_outclrmdir)
    def rmdir_logic():
        global is_root
        ls_outp = os.listdir()
        in_rmdir = True
        while in_rmdir == True:
            no_delete = {
                "tosapps"
                "tospycapps"
                "tosframeworklib"
                "boot.py"
                "trashloader.py"
                "calculator.py"
                "users.json"
                "__pycache__"
            }
            if is_root == True:
                rmdir_inp = input("rmdir: ")
                if os.path.exists(rmdir_inp):
                    shutil.rmtree(rmdir_inp)
                    ls_outclrmdir = ", ".join(os.listdir())
                    print(ls_outclrmdir)
                    in_rmdir = False
                else:
                    print(f"Directory {rmdir_inp} not found")
            elif is_root == False:
                rmdir_inp = input("rmdir: ")
                if rmdir_inp in no_delete:
                    print("Permission denied!")
                    in_rmdir = False
                else:
                    if os.path.exists(rmdir_inp):
                        shutil.rmtree(rmdir_inp)
                        ls_outclrmdir = ", ".join(os.listdir())
                        print(ls_outclrmdir)
                        in_rmdir = False
                    else:
                        print(f"Directory {rmdir_inp} not found")
    while True:
        prompt_text = f"{log_user}@TrashOS~ "
        app_path = "C:\\tossystem\\tosapps"
        input_cmd = input(prompt_text).strip().lower()
        if input_cmd == "help":
            print("""List of avalible commands:
            help - Lists all commands
            root - Puts user into root shell
            sudo - Runs command as root
            ver - Lists TrashOS Reborn version
            browser - Opens web browser
            files - Opens file browser
            calc - Opens calculator
            shutdown - Turns off the computer
            hostos - Displays the host OS
            echo - Prints text to the terminal
            changelog - Prints the latest changelogs
            usermgr - Puts you into the user manager
            ls - Lists subfolders and files
            mkdir - Creates directory
            rmdir - Removes directory
            rm - Removes file""")
        elif input_cmd == "root":
            root_pass = input("Password for user root: ")
            if root_pass == "root":
                is_root = True
                log_user = "root"
                print("User is root")
            else:
                print("Login failed for user root")
                
        elif input_cmd == "ver":
            print("""TrashOS Reborn version:
            1.1.0
            Security patch: SUBPRCSPTCH
            Bootloader: TrashLoader
            Bootloader ver: 1.0.2""")
        elif input_cmd == "calc":
            subprocess.run([sys.executable, "calculator.py"])
        elif input_cmd == "hostos":
            print(f"TrashOS reborn is running ontop of {host_os}")
        elif input_cmd == "browser":
            print("Opening web browser")
            webbrowser.open("https://google.com")
        elif input_cmd == "shutdown":
            print("Shutting down")
            time.sleep(0.5)
            print("RAMDISK unloaded")
            time.sleep(0.8)
            print("Bash unloaded")
            time.sleep(2)
            print("Unloading drivers")
            time.sleep(3.2)
            print("BIOS shutdown signal sent")
            time.sleep(0.3)
            print("Goodbye from TrashOS!")
            time.sleep(1.2)
            print("Unloaded kernel")
            time.sleep(2)
            sys.exit()
        elif input_cmd == "echo":
            echo_inp = input("echo:")
            print(echo_inp)
        elif input_cmd == "apps":
            striped_apps = apps_in_folder
            print(apps_in_folder)
        elif input_cmd == "numguess":
            guess_game()
        
        elif input_cmd == "changelog":
            print("""
            1.1.0 changes:
            Added user manager command
            Added Discord client TrashCord
            Added mkdir and ls commands
            Added logout command
            Added on boot sign in
            Added Pre Boot user for compatibility
            Added rmdir command""")
        elif input_cmd == "usrmgr":
            make_change_user()  
        elif input_cmd == "logout":
            print(f"Logging user {log_user} out")
            time.sleep(0.5)
            break
        elif input_cmd == "ls":
            work_dir = os.getcwd()
            ls_outp1 = os.listdir()
            ls_outcl = ", ".join(os.listdir())
            print(f"LS output of directory {work_dir}")
            print(ls_outcl)
        elif input_cmd == "mkdir":
            mkdir_logic()
        elif input_cmd == "rmdir":
            rmdir_logic()
        elif input_cmd == "rm":
            no_delete = {
                "tosapps"
                "tospycapps"
                "tosframeworklib"
                "boot.py"
                "trashloader.py"
                "calculator.py"
                "users.json"
                "__pycache__"
            }
            ls_outclrmdir = ", ".join(os.listdir())
            print(ls_outclrmdir)
            rm_inp = input("rm: ")
            if is_root == False:
                if rm_inp in no_delete:
                    print(f"Permission denied for file {rm_inp}")
                    
                if rm_inp not in no_delete:
                    rm_confirm = input(f"Confirm delete for file {rm_inp}? (y/n)").strip().lower()
                    if rm_confirm in ["y", "yes"]:
                            os.remove(rm_inp)
                            print(f"File {rm_inp} deleted")
                            print(ls_outclrmdir)
                    elif rm_confirm  in ["n", "no"]:
                        print("Deletion cancelled")
                    elif rm_confirm not in ["n", "y"]:
                        print("Invalid option")
            elif is_root == True:
                rm_confirm = input(f"Confirm delete for file {rm_inp}? (y/n)").strip().lower()
            if rm_confirm == "y":
                os.remove(rm_inp)
                print(f"File {rm_inp} deleted")
                print(ls_outclrmdir)
            elif rm_confirm not in ["n", "y"]:
                print("Deletion cancelled")
            else:
                print("Invalid option")
        elif input_cmd == "touch":
            print("add extension to input please")
            touch_inp = input("touch: ")
            Path(touch_inp).touch()
                
        else:
            app_exec = os.path.join(APPS_DIR, f"{input_cmd}.py")
            if os.path.exists(app_exec):
                import subprocess
                subprocess.run([sys.executable, app_exec])
            else:
                base_commands = "help","root","sudo","ver","browser","files", "calc", "shutdown", "hostos", "install", "changelog", "usermgr", "ls", "mkdir"
                all_possibilities = list(base_commands)
                apps_in_folder = [f.replace(".py", "") for f in os.listdir(APPS_DIR)]
                all_possibilities.extend(apps_in_folder)
                matches = difflib.get_close_matches(input_cmd, all_possibilities, n=1, cutoff=0.6)
                if matches:
                    print(f"Command {input_cmd} not found, Perhaps you meant {matches[0]}?")
                else:
                    print(f"Command {input_cmd} not found")
