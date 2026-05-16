import time
import sys
import json
import subprocess
import os
import webbrowser
import platform
host_os_type = platform.system()
host_os_release = platform.release()
host_os = f"{host_os_type} {host_os_release}"
base_commands = "help","root","sudo","ver","browser","files", "calc", "shutdown", "hostos", "install"
print("Booting system")

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
print("Welcome to TrashOS!")
time.sleep(0.8)
while True:
    input_cmd = input("root@TrashOS-Live~ ").strip().lower()
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
        install - Opens the TrashOS installer""")
    elif input_cmd == "root":
        print("Root is only user in Live CD")
    elif input_cmd == "sudo":
        print("You are already running as root!")
    elif input_cmd == "ver":
        print("""TrashOS Reborn
        Version 1.0.0
        Security patch: KRNLEX26ZD
        Enviorment: Disk
        Bootloader: TrashLoader
        Bootloader ver: 1.0.0
        Kernel version: 1.0.0 Release""")
    elif input_cmd == "calc":
        first_val = int(input("Enter first value: "))
        sec_val = int(input("Enter second value: "))
        answer = first_val + sec_val
        print(f"Answer to {first_val} + {sec_val} is: {answer}")
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
    elif input_cmd == "install":
        install_consent = input("Are you sure you want to install TrashOS on disk? (Y/N) ").upper()
        if install_consent == "Y":
            print("Test")
            print("Helo world")
            # no logic yet
        elif install_consent == "N":
            print("Install cancel")
            pass   