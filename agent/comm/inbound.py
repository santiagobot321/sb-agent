import socket
import threading
import json
from agent.sysadmin import executor

# Diccionario limpio: nada de frases mágicas estilo "shutdown now"
ACTIONS = {
    "shutdown": executor.shutdown,
    "upgrade": executor.update_system,
    "show_video": lambda args: executor.show_video(args.get("path")),
    "set_wallpaper": lambda args: executor.change_wallpaper(args.get("path")),
}

def handle(conn, addr):
    try:
        raw = conn.recv(4096).decode().strip()
        if not raw:
            print(f"[WARN] Empty payload from {addr}")
            return

        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            print(f"[WARN] Invalid JSON from {addr}: {raw}")
            return

        action = data.get("action")
        args = data.get("args", {})

        if action in ACTIONS:
            print(f"[INFO] Executing '{action}' from {addr} with args={args}")
            ACTIONS[action](args)
        else:
            print(f"[WARN] Unknown action '{action}' from {addr}")

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
