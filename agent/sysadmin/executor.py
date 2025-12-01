# agent/sysadmin/executor.py

import os
import subprocess

# ----------- POWER MANAGEMENT -------------

def shutdown():
    os.system("shutdown now")


# ----------- SYSTEM UPDATES ----------------

def update_system():
    subprocess.run("sudo apt update -y", shell=True, check=True)
    subprocess.run("sudo apt upgrade -y", shell=True, check=True)


# ----------- MULTIMEDIA --------------------

def show_video(video_path):
    subprocess.Popen(["xdg-open", video_path])



