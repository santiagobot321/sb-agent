# agent/core.py

import threading
import time
from agent.comm.inbound import listen
from agent.comm.outbound import send_status

def heartbeat(server_url, interval=30):
    while True:
        try:
            send_status(server_url)
        except Exception as e:
            print(f"[ERROR] heartbeat failed: {e}")
        time.sleep(interval)

def start(server_url):
    threading.Thread(target=heartbeat, args=(server_url,), daemon=True).start()
    listen()
