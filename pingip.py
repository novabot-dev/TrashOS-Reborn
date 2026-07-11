import subprocess
import platform
host_os_type = platform.system()




ping_target = input("Target address (e.g., google.com): ").strip()
if ping_target:
    print(f"Attempting ping on {ping_target}")
    ping_count = "-n" if host_os_type == "Windows" else "-c"
    try:
        subprocess.run(["ping", ping_count, "4", ping_target])
    except Exception as e:
        print(f"Ping failed to execute: {e}")
else:
    print("Invalid target!")