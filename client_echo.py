import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 65432))

while True:
    msg = input("Enter message (or 'exit'): ")
    if msg == "exit":
        break

    client.sendall(msg.encode())
    data = client.recv(1024)
    print("Echo:", data.decode())

client.close()