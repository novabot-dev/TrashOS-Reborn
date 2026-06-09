import os
import platform
import subprocess
import sys
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KERNEL_SCRIPT = os.path.join(BASE_DIR, "kernel.py")
TRASHLOADER_VER = "1.1.0"

BIOS_CONFIG = {
    "SGX": "Disabled",
    "Secure Boot": "Enabled",
}


def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def print_banner():
    clear_screen()
    print("========================================")
    print("          TrashLoader Boot Menu          ")
    print("========================================")
    print(f"Version: {TRASHLOADER_VER}")
    print(f"Host: {platform.system()} {platform.release()}")
    print("========================================\n")


def boot_menu():
    print("Boot options:")
    print("  1) TrashOS")
    print("  2) TrashOS with special CPU driver")
    print("  3) TrashOS in Safe Mode")
    print("  4) BIOS settings")
    print("  5) EFI shell")
    print("  6) Shutdown")
    print("  7) Refresh")
    print("  0) Exit bootloader")


def launch_boot(mode_label, mode_arg="normal"):
    print(f"\nStarting {mode_label}...")
    time.sleep(0.6)
    result = subprocess.run([sys.executable, KERNEL_SCRIPT, mode_arg])
    return result.returncode


def bios_menu():
    while True:
        clear_screen()
        print("BIOS Configuration")
        print("-------------------")
        for key, value in BIOS_CONFIG.items():
            print(f"{key}: {value}")
        print("\nType the name of the setting to toggle, or press Enter to return.")
        choice = input("Choice: ").strip()
        if not choice:
            return
        if choice in BIOS_CONFIG:
            BIOS_CONFIG[choice] = "Enabled" if BIOS_CONFIG[choice] == "Disabled" else "Disabled"
            print(f"{choice} set to {BIOS_CONFIG[choice]}")
            time.sleep(0.5)
        else:
            print("Unknown BIOS option.")
            time.sleep(0.5)


def efi_shell():
    shell_cmd = os.environ.get("COMSPEC" if platform.system() == "Windows" else "SHELL")
    if not shell_cmd:
        shell_cmd = "cmd.exe" if platform.system() == "Windows" else "/bin/sh"

    print(f"Opening host shell: {shell_cmd}")
    time.sleep(0.6)
    try:
        subprocess.run([shell_cmd])
    except Exception:
        subprocess.run(shell_cmd, shell=True)

    print("Host shell closed. Returning to TrashLoader...")
    time.sleep(0.5)


def shutdown():
    print("Shutting down TrashLoader...")
    time.sleep(0.8)
    print("TrashLoader unloaded")
    sys.exit(0)


def main():
    while True:
        print_banner()
        boot_menu()
        choice = input("Select boot option: ").strip()

        result = None
        handled = True
        if choice == "1":
            result = launch_boot("TrashOS", "normal")
        elif choice == "2":
            print("Loading TrashOS with special CPU driver")
            time.sleep(0.6)
            result = launch_boot("TrashOS with special CPU driver", "fast")
        elif choice == "3":
            print("Loading TrashOS in Safe Mode...")
            time.sleep(0.6)
            result = launch_boot("TrashOS Safe Mode", "safe")
        elif choice == "4":
            bios_menu()
        elif choice == "5":
            efi_shell()
        elif choice == "6":
            shutdown()
        elif choice == "7":
            continue
        elif choice == "0":
            print("Exiting TrashLoader.")
            time.sleep(0.4)
            break
        else:
            handled = False

        if not handled:
            print("Invalid selection. Please choose a valid boot option.")
            time.sleep(0.6)
            continue

        if result == 99:
            print("System shutdown complete. Exiting TrashLoader.")
            time.sleep(0.6)
            sys.exit(0)
        elif result == 100:
            print("Bootloader restart requested. Returning to TrashLoader...")
            time.sleep(0.6)
            continue


if __name__ == "__main__":
    main()