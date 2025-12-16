import socket
from threading import Thread

def handle_client(conn, addr):
    print(f"Connected: {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
    conn.close()
    print(f"Disconnected: {addr}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 65432))
server.listen()

print("Echo server is running...")

while True:
    conn, addr = server.accept()
    thread = Thread(target=handle_client, args=(conn, addr))
    thread.start()

#sudo kill -9 pid#
#sudo lsof -i :65432