# sysinfo_collector.py
# Simple local system info collector (safe to run locally)

import platform
import socket
import os
import shutil
import datetime
import getpass

def bytes_to_gb(n):
    return f"{n / 1024**3:.2f} GB"

def collect():
    info = {
        "timestamp_utc": datetime.datetime.utcnow().isoformat() + "Z",
        "user": getpass.getuser(),
        "hostname": socket.gethostname(),
        "os": platform.platform(),
        "architecture": platform.machine(),
        "python_version": platform.python_version(),
        "cpu_count": os.cpu_count(),
    }
    try:
        total, used, free = shutil.disk_usage(os.path.abspath(os.sep))
        info.update({
            "disk_total": bytes_to_gb(total),
            "disk_used": bytes_to_gb(used),
            "disk_free": bytes_to_gb(free),
        })
    except Exception:
        pass
    return info

if __name__ == "__main__":
    data = collect()
    for k, v in data.items():
        print(f"{k}: {v}")
