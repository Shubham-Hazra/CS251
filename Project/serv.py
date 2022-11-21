import socket
from msg import *
import pickle,json

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 5001  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(4096)
            message = pickle.loads(data)
            print(message.msg)
            if not data:
                break
            conn.sendall(data)
