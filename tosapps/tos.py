"""TrashOS app framework.

Apps can import this module to:
- check root state with is_root()
- clear the terminal with term.cls()
- store app-specific data with appdata.path()
- inspect host OS and hardware via system
- execute commands with shell.run() or run()
"""

import os
import sys
import platform
import json
import subprocess

current_dir = os.path.dirname(os.path.abspath(__file__))

if os.path.basename(current_dir) == "tosapps":
    base_dir = os.path.dirname(current_dir)
else:
    base_dir = current_dir

appdata_root = os.path.join(base_dir, "appdata")
STATUS_API_FILE = os.path.join(base_dir, "tosapi_status.json")

if not os.path.exists(appdata_root):
    os.makedirs(appdata_root)

_cached_status = {"version": "1.0.0", "is_root": False}
_last_mtime = 0

def _read_api_status():
    global _cached_status, _last_mtime
    if os.path.exists(STATUS_API_FILE):
        try:
            current_mtime = os.path.getmtime(STATUS_API_FILE)
            if current_mtime != _last_mtime:
                with open(STATUS_API_FILE, "r") as f:
                    _cached_status = json.load(f)
                _last_mtime = current_mtime
        except:
            pass
    return _cached_status

def is_root():
    status = _read_api_status()
    return status.get("is_root", False)

api_status = _read_api_status

class Status:
    @staticmethod
    def get():
        return _read_api_status()

    @staticmethod
    def is_root():
        return _read_api_status().get("is_root", False)

    @staticmethod
    def version():
        return _read_api_status().get("version", "1.0.0")

class AppData:
    """App storage helpers for TrashOS apps."""

    def path(self, app_name, *parts):
        specific_path = os.path.join(appdata_root, app_name, *parts)
        directory = os.path.dirname(specific_path) if parts else specific_path
        os.makedirs(directory, exist_ok=True)
        return specific_path

    def file(self, app_name, filename):
        file_path = self.path(app_name, filename)
        if not os.path.exists(file_path):
            open(file_path, "a").close()
        return file_path

    def read(self, app_name, filename, encoding="utf-8"):
        file_path = self.file(app_name, filename)
        with open(file_path, "r", encoding=encoding, errors="ignore") as f:
            return f.read()

    def write(self, app_name, filename, content, encoding="utf-8"):
        file_path = self.path(app_name, filename)
        with open(file_path, "w", encoding=encoding) as f:
            f.write(content)
        return file_path

    def exists(self, app_name, *parts):
        return os.path.exists(self.path(app_name, *parts))

    def ensure(self, app_name):
        return self.path(app_name)

class Terminal:
    """Terminal helpers for TrashOS apps."""

    def cls(self):
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    def title(self, title):
        if platform.system() == "Windows":
            os.system(f"title {title}")

    def clear(self):
        return self.cls()

class System:
    @staticmethod
    def is_windows():
        return platform.system() == "Windows"

    @staticmethod
    def is_linux():
        return platform.system() == "Linux"

    @staticmethod
    def is_macos():
        return platform.system() == "Darwin"

    @staticmethod
    def host_os():
        return f"{platform.system()} {platform.release()}"

    @staticmethod
    def cpu():
        try:
            if System.is_windows():
                raw_cpu = subprocess.check_output("wmic cpu get name", shell=True, stderr=subprocess.DEVNULL)
                lines = [line.strip() for line in raw_cpu.decode(errors="ignore").splitlines() if line.strip()]
                return next((line for line in lines if line.lower() != "name"), "Unknown CPU")
            if System.is_linux():
                raw_cpu = subprocess.check_output(["lscpu"], text=True, stderr=subprocess.DEVNULL)
                for line in raw_cpu.splitlines():
                    if line.startswith("Model name:"):
                        return line.split(":", 1)[1].strip()
                with open("/proc/cpuinfo", "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        if line.startswith("model name"):
                            return line.split(":", 1)[1].strip()
            if System.is_macos():
                raw_cpu = subprocess.check_output(["sysctl", "-n", "machdep.cpu.brand_string"], text=True, stderr=subprocess.DEVNULL)
                return raw_cpu.strip()
        except Exception:
            pass
        return "Unknown CPU"

    @staticmethod
    def gpu():
        try:
            if System.is_windows():
                raw_gpu = subprocess.check_output("wmic path Win32_VideoController get name", shell=True, stderr=subprocess.DEVNULL)
                lines = [line.strip() for line in raw_gpu.decode(errors="ignore").splitlines() if line.strip()]
                return next((line for line in lines if line.lower() != "name"), "Unknown GPU")
            if System.is_linux():
                raw_gpu = subprocess.check_output(["lspci"], text=True, stderr=subprocess.DEVNULL)
                for line in raw_gpu.splitlines():
                    if any(keyword in line for keyword in ["VGA compatible controller", "3D controller", "Display controller"]):
                        return line.split(":", 1)[1].strip()
                raw_gpu = subprocess.check_output(["glxinfo"], text=True, stderr=subprocess.DEVNULL)
                for line in raw_gpu.splitlines():
                    if "OpenGL renderer string:" in line:
                        return line.split(":", 1)[1].strip()
            if System.is_macos():
                raw_gpu = subprocess.check_output(["system_profiler", "SPDisplaysDataType"], text=True, stderr=subprocess.DEVNULL)
                for line in raw_gpu.splitlines():
                    if "Chipset Model:" in line:
                        return line.split(":", 1)[1].strip()
                    if "Model:" in line:
                        return line.split(":", 1)[1].strip()
        except Exception:
            pass
        return "Unknown GPU"

class Shell:
    @staticmethod
    def run(command, capture=False, shell=False):
        if capture:
            return subprocess.check_output(command, shell=shell, text=True, stderr=subprocess.DEVNULL).strip()
        subprocess.run(command, shell=shell)

    @staticmethod
    def capture(command, shell=False):
        return Shell.run(command, capture=True, shell=shell)

    @staticmethod
    def execute(command, shell=False):
        return Shell.run(command, capture=False, shell=shell)


def run(command, capture=False, shell=False):
    return Shell.run(command, capture=capture, shell=shell)

appdata = AppData()
term = Terminal()
system = System()
shell = Shell()

class DynamicVersionModule(sys.modules[__name__].__class__):
    @property
    def version(self):
        status = _read_api_status()
        return status.get("version", "1.0.0")

sys.modules[__name__].__class__ = DynamicVersionModule