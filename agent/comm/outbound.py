import socket
import requests
import uuid
from agent.security.netstats import is_in_lan, is_online

# Generamos un ID persistente. Ideal guardarlo en un archivo local.
AGENT_ID = str(uuid.uuid4())

def send_status(server_url):
    payload = {
        "agent_id": AGENT_ID,
        "hostname": socket.gethostname(),
        "ip": socket.gethostbyname(socket.gethostname()),
        "lan": is_in_lan(),
        "internet": is_online(),
    }

    try:
        requests.post(server_url, json=payload, timeout=5)
    except Exception as e:
        print(f"[ERROR] outbound failed: {e}")

    return payload
