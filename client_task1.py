import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b"Hello via UDP!", (HOST, PORT))
    
    data, addr = s.recvfrom(1024)
    print(f"Received from server: {data}")