import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print("UDP server is running...")
    
    while True:
        data, addr = s.recvfrom(1024)
        print(f"Received from {addr}: {data}")
        
        # Echo response
        s.sendto(data, addr)

#sudo kill -9 pid#
#sudo lsof -i :65432
