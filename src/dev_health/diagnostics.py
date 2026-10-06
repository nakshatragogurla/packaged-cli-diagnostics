import os
import shutil
import subprocess
import sys


def get_python_info():
    return {
        "version": sys.version.split()[0],
        "status": "pass"
    }


def get_disk_info():
    total, used, free = shutil.disk_usage(os.getcwd())

    free_gb = round(free / (1024 ** 3), 2)

    return {
        "free_gb": free_gb,
        "status": "pass" if free_gb >= 1 else "warn"
    }


def get_environment_info():
    return {
        "PATH": "set" if os.environ.get("PATH") else "missing",
        "HOME": "set" if os.environ.get("HOME") else "missing"
    }


def get_tool_version(command):
    try:
        result = subprocess.run(
            [command, "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.returncode == 0:
            version = (result.stdout or result.stderr).strip()

            return {
                "installed": True,
                "version": version
            }

        return {
            "installed": False,
            "version": None
        }

    except (FileNotFoundError, subprocess.TimeoutExpired):
        return {
            "installed": False,
            "version": None
        }


def run_diagnostics():
    return {
        "python": get_python_info(),
        "disk": get_disk_info(),
        "environment": get_environment_info(),
        "tools": {
            "git": get_tool_version("git"),
            "node": get_tool_version("node"),
            "npm": get_tool_version("npm"),
            "java": get_tool_version("java")
        }
    }


def validate_config_path(path):
    if not isinstance(path, str) or not path.strip():
        return False

    if not os.path.isabs(path):
        return False

    return os.path.exists(path)