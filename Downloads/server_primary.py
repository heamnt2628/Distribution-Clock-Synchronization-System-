import socket
import time

# Server configuration
SERVER_IP = "0.0.0.0"   
PORT = 5000            

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, PORT))

print("=== Primary Time Server Running ===")

# Server runs continuously
while True:
    data, addr = sock.recvfrom(1024)      
    server_time = time.time()  
    print(f"✔ Request received from {addr}")
    sock.sendto(str(server_time).encode(), addr)