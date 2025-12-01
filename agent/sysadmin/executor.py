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

    env = os.environ.copy()
    env["DISPLAY"] = ":0"

    # Detect XAUTHORITY for GNOME/GDM
    if "XAUTHORITY" not in env or not os.path.exists(env.get("XAUTHORITY", "")):
        posible_xauth = f"/run/user/{os.getuid()}/gdm/Xauthority"
        if os.path.exists(posible_xauth):
            env["XAUTHORITY"] = posible_xauth

    try:
        subprocess.Popen(["xdg-open", video_path], env=env)
        print(f"[INFO] Video opened: {video_path}")
    except Exception as e:
        print(f"[ERROR] Could not open video: {e}")




