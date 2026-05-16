import time
import subprocess
import sys
print("SGX disabled or unsupported by BIOS")
time.sleep(0.5)
print("Loaded TrashLoader")
time.sleep(0.2)
print("Welcome to TrashLoader")
time.sleep(0.1)
print("Version 1.0.2")
while True:
    print("Boot options")
    print("1: TrashOS")
    print("2: TrashOS with special CPU driver")
    print("3: TrashOS with Safe Mode")
    print("4: BIOS")
    print("5: EFI shell")
    print("6: Shutdown")
    
    boot_option = input()
    if boot_option == "1":
        subprocess.run([sys.executable, "boot.py"])
    elif boot_option == "2":
        subprocess.run([sys.executable, "boot.py"])
    elif boot_option == "3":
        subprocess.run([sys.executable, "boot.py"])
    elif boot_option == "4":
        print("BIOS options")
        sgx_stat = "Disabled"
        sec_boot = "Enabled"
        print("SGX:", sgx_stat)
        print("Secure boot:", sec_boot)
        print("Press 1 to edit")
        kb_press = input("Type 1 to change value of SGX, 2 to change value of Secure Boot ")
        if kb_press == "1":
            sgx_stat = "Enabled"
        elif kb_press == "2":
            sec_boot = "Disabled"
        else:
            print("Non valid, rebooting")
            pass
    elif boot_option == "5":
        print("EFI shell unavalible")
        time.sleep(0.2)
        print("Rebooting")
        pass
    elif boot_option == "6":
        print("Shutting down")
        time.sleep(0.8)
        print("TrashLoader unloaded")
        sys.exit()
        break