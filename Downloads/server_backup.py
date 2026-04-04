import socket
import time

# Backup server configuration
SERVER_IP = "0.0.0.0"
PORT = 6000   

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to IP and port
sock.bind((SERVER_IP, PORT))

print("=== Backup Server Running ===")

# Run continuously
while True:
    data, addr = sock.recvfrom(1024)
    server_time = time.time()
    print(f"[Backup] Request received from {addr}")
    sock.sendto(str(server_time).encode(), addr)