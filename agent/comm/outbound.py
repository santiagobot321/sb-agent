import socket
import requests
from agent.security.netstats import is_in_lan, is_online

def send_status(server_url):
    payload = {
        "hostname": socket.gethostname(),
        "ip": socket.gethostbyname(socket.gethostname()),
        "lan": is_in_lan(),
        "internet": is_online()
    }

    try:
        requests.post(server_url, json=payload, timeout=5)
    except Exception as e:
        print(f"[ERROR] outbound failed: {e}")

    return payload
