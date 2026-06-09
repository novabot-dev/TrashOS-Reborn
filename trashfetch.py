import platform
import subprocess
import json
f = open("version.json", "r")
data = json.load(f)
f.close()
tosv = data
host_os_type = platform.system()
os_ver = platform.release()
def get_cpu_info():
    try:
        if host_os_type == "Windows":
            raw_cpu = subprocess.check_output("wmic cpu get name", shell=True, stderr=subprocess.DEVNULL)
            lines = [line.strip() for line in raw_cpu.decode(errors="ignore").splitlines() if line.strip()]
            for line in lines:
                if line.lower() != "name":
                    return line
        elif host_os_type == "Linux":
            try:
                raw_cpu = subprocess.check_output(["lscpu"], text=True, stderr=subprocess.DEVNULL)
                for line in raw_cpu.splitlines():
                    if line.startswith("Model name:"):
                        return line.split(":", 1)[1].strip()
            except (FileNotFoundError, subprocess.CalledProcessError):
                pass
            try:
                with open("/proc/cpuinfo", "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        if line.startswith("model name"):
                            return line.split(":", 1)[1].strip()
            except OSError:
                pass
        elif host_os_type == "Darwin":
            raw_cpu = subprocess.check_output(["sysctl", "-n", "machdep.cpu.brand_string"], text=True, stderr=subprocess.DEVNULL)
            return raw_cpu.strip()
    except Exception:
        pass
    return "Generic processor"


def get_gpu_info():
    try:
        if host_os_type == "Windows":
            raw_gpu = subprocess.check_output("wmic path Win32_VideoController get name", shell=True, stderr=subprocess.DEVNULL)
            lines = [line.strip() for line in raw_gpu.decode(errors="ignore").splitlines() if line.strip()]
            for line in lines:
                if line.lower() != "name":
                    return line
        elif host_os_type == "Linux":
            try:
                raw_gpu = subprocess.check_output(["lspci"], text=True, stderr=subprocess.DEVNULL)
                for line in raw_gpu.splitlines():
                    if any(keyword in line for keyword in ["VGA compatible controller", "3D controller", "Display controller"]):
                        return line.split(":", 1)[1].strip()
            except (FileNotFoundError, subprocess.CalledProcessError):
                pass
            try:
                raw_gpu = subprocess.check_output(["glxinfo"], text=True, stderr=subprocess.DEVNULL)
                for line in raw_gpu.splitlines():
                    if "OpenGL renderer string:" in line:
                        return line.split(":", 1)[1].strip()
            except (FileNotFoundError, subprocess.CalledProcessError):
                pass
        elif host_os_type == "Darwin":
            raw_gpu = subprocess.check_output(["system_profiler", "SPDisplaysDataType"], text=True, stderr=subprocess.DEVNULL)
            for line in raw_gpu.splitlines():
                if "Chipset Model:" in line:
                    return line.split(":", 1)[1].strip()
                if "Model:" in line:
                    return line.split(":", 1)[1].strip()
    except Exception:
        pass
    return "Generic software renderer"

cpu_text_clean = get_cpu_info()
gpu_text_clean = get_gpu_info()
print(f"""
T                 T    GPU: {gpu_text_clean}
 T---------------T     CPU: {cpu_text_clean}
  T   TrashOS   T      Host OS: {host_os_type} {os_ver}
   T-----------T       TrashOS version: {tosv}
    T Reborn  T        https://github.com/novabot-dev/TrashOS-Reborn
     T-------T         Made with love!!
      TTTTTT""")