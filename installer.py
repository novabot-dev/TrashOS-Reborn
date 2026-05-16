import os
import sys
import shutil
import time

print("""------------------------
TrashOS installer
------------------------""")

if os.name == 'nt':
    try:
        drives = os.listdrives()
        print(f"Available drives: {', '.join(drives)}")
        target_drive = drives[0]
    except AttributeError:
        target_drive = "C:\\"
else:
    target_drive = os.path.expanduser("~")

final_consent = input(f"Confirm install on {target_drive}? (Y/N) ").upper()

if final_consent == "Y":
    install_path = os.path.join(target_drive, "tossystem")
    folders = [
        "tospycapps",
        "appdata",
        "tosapps",
        "tosframeworklib"
    ]
    
    print(f"\n[!] Creating system partitions at {install_path}...")

    for folder in folders:
        full_path = os.path.join(install_path, folder)
        if not os.path.exists(full_path):
            os.makedirs(full_path)
            print(f"   -> Created {folder}")
            time.sleep(0.5)
    print("\n[OK] Partitioning done")
    print(f"Please copy boot.py and trashloader.py into {install_path}!")

elif final_consent == "N":
    print("Install canceled")
    time.sleep(0.2)
    sys.exit()