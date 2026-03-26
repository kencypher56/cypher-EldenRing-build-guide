"""
setup.py - System setup, environment creation, package installation, and model download
for Cypher Elden Ring Build Guide
"""

import os
import sys
import shutil
import subprocess
import platform
import time

# ── Terminal colors (no rich dependency here) ─────────────────────────────────
GOLD   = "\033[93m"
GREEN  = "\033[92m"
RED    = "\033[91m"
CYAN   = "\033[96m"
DIM    = "\033[2m"
RESET  = "\033[0m"
BOLD   = "\033[1m"

def p(msg, color=GOLD):   print(f"{color}{msg}{RESET}")
def ok(msg):              print(f"{GREEN}  ✓ {msg}{RESET}")
def err(msg):             print(f"{RED}  ✗ {msg}{RESET}")
def info(msg):            print(f"{CYAN}  ➤ {msg}{RESET}")
def dim(msg):             print(f"{DIM}    {msg}{RESET}")


BANNER = f"""{GOLD}
  ╔══════════════════════════════════════════════════════╗
  ║       CYPHER ELDEN RING BUILD GUIDE — SETUP          ║
  ║            deepseek-r1:8b · Ollama · Python          ║
  ╚══════════════════════════════════════════════════════╝
{RESET}"""

REQUIRED_PACKAGES = [
    "rich",
    "requests",
    "reportlab",
    "psutil",
]

ENV_NAME = "cypher-eldenring"
MODEL_NAME = "deepseek-r1:8b"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


# ── System Detection ──────────────────────────────────────────────────────────
def detect_system():
    """Basic system detection for setup purposes."""
    system = platform.system()
    machine = platform.machine()
    py_ver = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"

    info(f"OS: {system} {platform.release()} ({machine})")
    info(f"Python: {py_ver} at {sys.executable}")

    # Check CUDA via nvidia-smi
    has_gpu = False
    if shutil.which("nvidia-smi"):
        try:
            result = subprocess.run(
                ["nvidia-smi", "--query-gpu=name", "--format=csv,noheader"],
                capture_output=True, text=True, timeout=8
            )
            if result.returncode == 0:
                gpus = result.stdout.strip().split("\n")
                for g in gpus:
                    ok(f"GPU detected: {g.strip()}")
                has_gpu = True
        except Exception:
            pass

    if not has_gpu:
        info("No NVIDIA GPU detected — will use CPU mode.")

    return {"system": system, "has_gpu": has_gpu}


# ── Ollama Detection & Model Setup ────────────────────────────────────────────
def check_ollama():
    """Check if Ollama is installed and offer to start it."""
    p("\n⚙ Checking Ollama...")
    ollama_path = shutil.which("ollama")

    if not ollama_path:
        err("Ollama is not installed or not in PATH.")
        print()
        p("  Please install Ollama from: https://ollama.com/download", CYAN)
        p("  Then run this setup again.", CYAN)
        return False

    ok(f"Ollama found at: {ollama_path}")

    # Check if running
    try:
        import urllib.request
        urllib.request.urlopen("http://localhost:11434", timeout=3)
        ok("Ollama server is running.")
        return True
    except Exception:
        pass

    info("Ollama is not running. Attempting to start it in background...")
    try:
        if platform.system() == "Windows":
            subprocess.Popen(
                ["ollama", "serve"],
                creationflags=subprocess.CREATE_NEW_CONSOLE,
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            )
        else:
            subprocess.Popen(
                ["ollama", "serve"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True,
            )
        print("  Waiting for Ollama to start", end="", flush=True)
        for _ in range(15):
            time.sleep(1)
            print(".", end="", flush=True)
            try:
                import urllib.request
                urllib.request.urlopen("http://localhost:11434", timeout=2)
                print()
                ok("Ollama server started successfully.")
                return True
            except Exception:
                continue
        print()
        err("Ollama did not start in time. Start it manually: ollama serve")
        return False
    except Exception as e:
        err(f"Could not start Ollama: {e}")
        return False


def pull_model():
    """Pull the deepseek-r1:8b model if not already present."""
    p(f"\n⚙ Checking for model: {MODEL_NAME}...")

    try:
        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True, text=True, timeout=10
        )
        if MODEL_NAME.split(":")[0] in result.stdout or MODEL_NAME in result.stdout:
            ok(f"Model {MODEL_NAME} is already available.")
            return True
    except Exception:
        pass

    info(f"Model {MODEL_NAME} not found. Pulling now (this may take several minutes)...")
    info("The model is ~4.9GB. Please be patient, Tarnished.")
    print()

    try:
        result = subprocess.run(
            ["ollama", "pull", MODEL_NAME],
            timeout=1800,  # 30 min max
        )
        if result.returncode == 0:
            ok(f"Model {MODEL_NAME} pulled successfully.")
            return True
        else:
            err(f"Failed to pull model (exit code {result.returncode}).")
            return False
    except subprocess.TimeoutExpired:
        err("Model download timed out. Run manually: ollama pull deepseek-r1:8b")
        return False
    except Exception as e:
        err(f"Error pulling model: {e}")
        return False


# ── Package Installation ──────────────────────────────────────────────────────
def install_packages_pip():
    """Install required packages using pip."""
    p("\n⚙ Installing Python packages via pip...")
    for pkg in REQUIRED_PACKAGES:
        info(f"Installing {pkg}...")
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "--quiet", "--upgrade", pkg],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            ok(f"{pkg} installed.")
        else:
            err(f"Failed to install {pkg}: {result.stderr[:200]}")


def install_packages_conda(env_name: str):
    """Create conda environment and install packages."""
    conda_path = shutil.which("conda")
    if not conda_path:
        return False

    p(f"\n⚙ Creating conda environment: {env_name}...")

    # Check if env already exists
    result = subprocess.run(
        ["conda", "env", "list"],
        capture_output=True, text=True
    )
    if env_name in result.stdout:
        ok(f"Conda environment '{env_name}' already exists.")
    else:
        result = subprocess.run(
            ["conda", "create", "-n", env_name, "python=3.10", "-y", "--quiet"],
        )
        if result.returncode != 0:
            err("Failed to create conda environment.")
            return False
        ok(f"Conda environment '{env_name}' created.")

    # Get the python path in the conda env
    if platform.system() == "Windows":
        env_python = os.path.join(
            os.path.dirname(conda_path), "envs", env_name, "python.exe"
        )
        if not os.path.exists(env_python):
            env_python = subprocess.run(
                ["conda", "run", "-n", env_name, "which", "python"],
                capture_output=True, text=True
            ).stdout.strip()
    else:
        result = subprocess.run(
            ["conda", "run", "-n", env_name, "which", "python"],
            capture_output=True, text=True
        )
        env_python = result.stdout.strip()

    if not env_python or not os.path.exists(env_python):
        info("Could not locate conda env python; falling back to current python.")
        install_packages_pip()
        return True

    info(f"Installing packages in conda env using: {env_python}")
    for pkg in REQUIRED_PACKAGES:
        result = subprocess.run(
            [env_python, "-m", "pip", "install", "--quiet", "--upgrade", pkg],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            ok(f"{pkg} installed in conda env.")
        else:
            err(f"Failed to install {pkg}: {result.stderr[:200]}")

    return True


def create_venv():
    """Create a virtual environment as fallback."""
    venv_path = os.path.join(SCRIPT_DIR, ".venv")
    p(f"\n⚙ Creating virtual environment at {venv_path}...")

    if os.path.exists(venv_path):
        ok("Virtual environment already exists.")
    else:
        result = subprocess.run(
            [sys.executable, "-m", "venv", venv_path],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            err(f"Failed to create venv: {result.stderr}")
            return None
        ok("Virtual environment created.")

    # Determine pip path
    if platform.system() == "Windows":
        pip_path = os.path.join(venv_path, "Scripts", "pip.exe")
        python_path = os.path.join(venv_path, "Scripts", "python.exe")
    else:
        pip_path = os.path.join(venv_path, "bin", "pip")
        python_path = os.path.join(venv_path, "bin", "python")

    for pkg in REQUIRED_PACKAGES:
        result = subprocess.run(
            [pip_path, "install", "--quiet", "--upgrade", pkg],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            ok(f"{pkg} installed in venv.")
        else:
            err(f"Failed to install {pkg}")

    return venv_path


# ── Main Setup ────────────────────────────────────────────────────────────────
def main():
    print(BANNER)
    p("  Initializing setup for Cypher Elden Ring Build Guide...\n")

    # System info
    p("⚙ Detecting system...")
    sys_info = detect_system()

    # Choose installation method
    print()
    p("⚙ Environment Setup")
    print(f"  {GOLD}Choose your installation method:{RESET}")
    print(f"  {CYAN}  1) Conda  — create '{ENV_NAME}' conda environment (recommended){RESET}")
    print(f"  {CYAN}  2) venv   — create local .venv virtual environment{RESET}")
    print(f"  {CYAN}  3) pip    — install packages into current Python environment{RESET}")
    print()

    try:
        choice = input(f"  {GOLD}Enter choice [1/2/3, default=1]: {RESET}").strip() or "1"
    except KeyboardInterrupt:
        p("\n\n  Setup cancelled. The flame fades...", RED)
        sys.exit(0)

    if choice == "1":
        if shutil.which("conda"):
            success = install_packages_conda(ENV_NAME)
            if not success:
                info("Conda install failed. Falling back to pip...")
                install_packages_pip()
        else:
            err("Conda not found. Falling back to venv...")
            create_venv()
    elif choice == "2":
        venv = create_venv()
        if not venv:
            info("venv failed. Falling back to pip...")
            install_packages_pip()
        else:
            ok(f"venv created at {venv}")
            if platform.system() == "Windows":
                activate = os.path.join(venv, "Scripts", "activate")
            else:
                activate = f"source {os.path.join(venv, 'bin', 'activate')}"
            info(f"To activate: {activate}")
    else:
        install_packages_pip()

    # Ollama setup
    ollama_ok = check_ollama()

    if ollama_ok:
        pull_model()
    else:
        p("\n  ⚠ Skipping model download — Ollama not available.", "\033[93m")
        p("  Install Ollama then run: ollama pull deepseek-r1:8b", CYAN)

    # Final summary
    print()
    p("══════════════════════════════════════════════════════")
    p("  SETUP COMPLETE!", GREEN)
    p("══════════════════════════════════════════════════════")
    print()
    ok("All packages installed")
    ok("System detection ready")
    if ollama_ok:
        ok("Ollama configured")
    else:
        err("Ollama requires manual setup")
    print()
    p("  To start the build generator:", CYAN)
    p("      python run.py", BOLD)
    print()
    p("  May grace guide thee, Tarnished. ✦", GOLD)
    print()


if __name__ == "__main__":
    main()