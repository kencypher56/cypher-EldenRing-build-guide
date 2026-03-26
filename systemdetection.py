"""
systemdetection.py - Detects OS, GPU, CUDA, and CPU for Cypher Elden Ring Build Guide
"""

import platform
import subprocess
import shutil
import sys
import os


def detect_os() -> dict:
    """Detect the operating system details."""
    return {
        "system": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
    }


def detect_cpu() -> dict:
    """Detect CPU information."""
    cpu_info = {
        "physical_cores": None,
        "logical_cores": None,
        "name": platform.processor() or "Unknown",
    }
    try:
        import psutil
        cpu_info["physical_cores"] = psutil.cpu_count(logical=False)
        cpu_info["logical_cores"] = psutil.cpu_count(logical=True)
    except ImportError:
        try:
            import os
            cpu_info["logical_cores"] = os.cpu_count()
        except Exception:
            pass
    return cpu_info


def detect_cuda() -> dict:
    """Detect CUDA availability."""
    cuda_info = {
        "available": False,
        "version": None,
        "device_count": 0,
        "devices": [],
    }

    # Check via nvidia-smi
    if shutil.which("nvidia-smi"):
        try:
            result = subprocess.run(
                ["nvidia-smi", "--query-gpu=name,memory.total,driver_version",
                 "--format=csv,noheader,nounits"],
                capture_output=True, text=True, timeout=10
            )
            if result.returncode == 0:
                cuda_info["available"] = True
                lines = result.stdout.strip().split("\n")
                cuda_info["device_count"] = len(lines)
                for line in lines:
                    parts = [p.strip() for p in line.split(",")]
                    if len(parts) >= 3:
                        cuda_info["devices"].append({
                            "name": parts[0],
                            "memory_mb": parts[1],
                            "driver": parts[2],
                        })
        except Exception:
            pass

    # Check via PyTorch
    try:
        import torch
        if torch.cuda.is_available():
            cuda_info["available"] = True
            cuda_info["version"] = torch.version.cuda
            cuda_info["device_count"] = torch.cuda.device_count()
            if not cuda_info["devices"]:
                for i in range(cuda_info["device_count"]):
                    props = torch.cuda.get_device_properties(i)
                    cuda_info["devices"].append({
                        "name": props.name,
                        "memory_mb": props.total_memory // (1024 * 1024),
                        "driver": "PyTorch detected",
                    })
    except ImportError:
        pass

    return cuda_info


def detect_ollama() -> dict:
    """Detect if Ollama is installed and running."""
    ollama_info = {
        "installed": False,
        "path": None,
        "running": False,
        "models": [],
    }

    ollama_path = shutil.which("ollama")
    if ollama_path:
        ollama_info["installed"] = True
        ollama_info["path"] = ollama_path

        try:
            result = subprocess.run(
                ["ollama", "list"],
                capture_output=True, text=True, timeout=10
            )
            if result.returncode == 0:
                ollama_info["running"] = True
                lines = result.stdout.strip().split("\n")
                for line in lines[1:]:  # Skip header
                    parts = line.split()
                    if parts:
                        ollama_info["models"].append(parts[0])
        except Exception:
            pass

    return ollama_info


def detect_model(model_name: str = "deepseek-r1:8b") -> dict:
    """Check if a specific Ollama model is available."""
    ollama = detect_ollama()
    return {
        "model": model_name,
        "available": any(model_name in m for m in ollama.get("models", [])),
        "ollama_running": ollama.get("running", False),
    }


def get_full_system_info() -> dict:
    """Get complete system information."""
    return {
        "os": detect_os(),
        "cpu": detect_cpu(),
        "cuda": detect_cuda(),
        "ollama": detect_ollama(),
        "python": {
            "version": sys.version,
            "executable": sys.executable,
        },
    }


def get_ollama_device_flag() -> str:
    """Return the best device string for Ollama (GPU if available, else CPU)."""
    cuda = detect_cuda()
    if cuda["available"] and cuda["device_count"] > 0:
        return "gpu"
    return "cpu"


if __name__ == "__main__":
    import json
    info = get_full_system_info()
    print(json.dumps(info, indent=2))