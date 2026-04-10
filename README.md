⏱️ Distributed Clock Synchronization System using UDP

📌 Project Overview
This project implements a **Distributed Clock Synchronization System** using UDP (User Datagram Protocol). It ensures that multiple client systems maintain consistent time by synchronizing with a central time server.

In distributed systems, each machine has its own internal clock, which may drift over time. This project solves that problem using a lightweight synchronization mechanism based on **Cristian’s Algorithm**.

---

🎯 Features

- 🟢 UDP-based communication (fast and lightweight)
- 🧠 Clock synchronization using Cristian’s Algorithm
- 🔄 Automatic switching to Backup Server (fault tolerance)
- ⚡ Delay (RTT) and Offset calculation
- 🧪 Drift simulation (real-world scenario)
- 📄 Logging of synchronization results


🏗️ System Architecture

      +----------------------+
      |   Primary Server     |
      |      (Port 5000)     |
      +----------+-----------+
                 |
    -----------------------------
    |            |             |
 Client1      Client2      Client3
                 |
      +----------------------+
      |   Backup Server      |
      |      (Port 6000)     |
      +----------------------+


## ⚙️ How It Works

1. Client sends a `TIME_REQUEST` to server
2. Server replies with current timestamp
3. Client calculates:
   - RTT (Round Trip Time)
   - Offset
4. Client adjusts its clock:
   

Adjusted Time = Server Time + (RTT / 2)


5. If primary server fails → switch to backup server

---

🧠 Algorithm Used

Cristian’s Algorithm
- Client sends request at time **T0**
- Receives response at **T1**
- Server time = **Ts**


RTT = T1 - T0
Adjusted Time = Ts + (RTT / 2)

🖥️ Requirements

Software
- Python 3.x
- OS: Windows / Linux
- 
Libraries Used
- socket
- time
- random (optional)
- hashlib (if secure version used)

⭐ Conclusion

This project demonstrates how distributed systems can maintain consistent time using lightweight UDP communication and synchronization algorithms. It highlights key networking concepts such as delay, drift, and fault tolerance.

