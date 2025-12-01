import socket
import threading
from agent.sysadmin import executor

COMMANDS = {
    "shutdown now": executor.shutdown,
    "upgrade": executor.update_system,
    "video": lambda: executor.show_video("/home/videos/welcome.mp4"),
    "wallpaper": lambda: executor.change_wallpaper("/home/images/wallpaper.png"),
}

def handle(conn, addr):
    try:
        raw = conn.recv(1024).decode().strip()
        action = COMMANDS.get(raw)

        if action:
            print(f"[INFO] Received command '{raw}' from {addr}")
            action()
        else:
            print(f"[WARN] Unknown command from {addr}: {raw}")
    except Exception as e:
        print(f"[ERROR] inbound handler failed: {e}")
    finally:
        conn.close()

def listen(port=9876):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", port))
    s.listen(5)

    print(f"[INFO] Inbound listener running on port {port}")

    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle, args=(conn, addr), daemon=True).start()
