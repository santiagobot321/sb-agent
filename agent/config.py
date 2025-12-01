import os
import socket
import uuid

def load_env(key, default=None):
    return os.environ.get(key, default)

SERVER_URL = load_env("SERVER_URL", "http://10.0.120.2:8000/agent")

# Si la máquina no tiene DEVICE_ID asignado, generamos uno estable
DEVICE_ID = load_env("DEVICE_ID", None)
if not DEVICE_ID:
    # Se genera un UUID basado en hardware (MAC) para que sea estático
    DEVICE_ID = str(uuid.uuid5(uuid.NAMESPACE_DNS, socket.gethostname()))

HEARTBEAT_INTERVAL = int(load_env("HEARTBEAT_INTERVAL", 30))
