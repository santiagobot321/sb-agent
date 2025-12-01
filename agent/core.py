# agent/core.py

import threading
import time
from agent.config import SERVER_URL, DEVICE_ID, HEARTBEAT_INTERVAL
from agent.comm.inbound import listen
from agent.comm.outbound import send_status

def heartbeat():
    while True:
        try:
            send_status(SERVER_URL, DEVICE_ID)
        except Exception as e:
            print(f"[ERROR] heartbeat failed: {e}")
        time.sleep(HEARTBEAT_INTERVAL)

def start():
    # Lanzar el heartbeat en segundo plano
    threading.Thread(target=heartbeat, daemon=True).start()

    # Comienza la escucha de comandos
    listen(SERVER_URL, DEVICE_ID)
