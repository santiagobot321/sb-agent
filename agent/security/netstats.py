# agent/security/netstats.py

import socket

def ping_host(ip, port=80, timeout=2):
    try:
        socket.create_connection((ip, port), timeout=timeout)
        return True
    except:
        return False

def is_in_lan(server_ip="10.0.120.27"):
    return ping_host(server_ip, 80)

def is_online():
    return ping_host("8.8.8.8", 53)
