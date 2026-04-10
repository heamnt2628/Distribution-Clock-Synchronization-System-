import socket
import time
import random

SERVER_IP = "10.125.101.155"

PRIMARY = (SERVER_IP, 5000)
BACKUP = (SERVER_IP, 6000)

def get_time(server):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(3)

    # Simulate clock drift
    drift = random.uniform(-3, 3)

    # Send request
    T0 = time.time() + drift
    sock.sendto(b"TIME_REQUEST", server)

    data, _ = sock.recvfrom(1024)

    # Receive time
    T1 = time.time() + drift

    server_time = float(data.decode())

    # Round Trip Time
    RTT = T1 - T0

    return server_time, RTT, T1

# Try primary server
try:
    server_time, RTT, local_time = get_time(PRIMARY)
    print("✔ Connected to Primary Server")

except Exception as e:
    print(f"⚠ Primary failed: {e}")
    print("➡ Switching to Backup...")

    try:
        server_time, RTT, local_time = get_time(BACKUP)
        print("✔ Connected to Backup Server")

    except Exception as e:
        print(f"❌ Backup also failed: {e}")
        exit()

# Smart delay filtering
if RTT > 1:
    print("❌ High delay detected, ignoring result")
    exit()

# Cristian’s Algorithm
adjusted_time = server_time + RTT / 2

# Offset calculation
offset = adjusted_time - local_time

# Output
print("\n=== Clock Synchronization Result ===")
print(f"Local Time   : {time.ctime(local_time)}")
print(f"Server Time  : {time.ctime(server_time)}")
print(f"Adjusted Time: {time.ctime(adjusted_time)}")
print(f"RTT Delay    : {RTT:.4f} sec")
print(f"Offset       : {offset:.4f} sec")

# Logging
with open("log.txt", "a") as f:
    f.write(f"{time.ctime()} | RTT={RTT:.4f} | Offset={offset:.4f}\n")

print("✔ Logged to log.txt")