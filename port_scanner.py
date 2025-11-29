import socket

target = input("Enter target IP: ")

print("\nScanning common ports...\n")
common_ports = [21, 22, 23, 80, 443, 445]

for port in common_ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN]  Port {port}")
    else:
        print(f"[CLOSED] Port {port}")
    s.close()
