import socket
from datetime import datetime

print("=" * 60)
print("      ADVANCED PORT SCANNER")
print("=" * 60)

target = input("Enter Target IP Address: ")
start_port = int(input("Enter Start Port: "))
end_port = int(input("Enter End Port: "))

start_time = datetime.now()

print("\nScanning Target:", target)
print("Started At:", start_time)
print("-" * 60)

open_ports = []

for port in range(start_port, end_port + 1):
    print(f"Checking Port {port}")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((target, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"

            print(f"[+] Port {port:<5} OPEN  | Service: {service}")
            open_ports.append((port, service))

        s.close()

    except KeyboardInterrupt:
        print("\nScan Interrupted")
        break

    except Exception:
        pass

end_time = datetime.now()

print("\n" + "=" * 60)
print("SCAN SUMMARY")
print("=" * 60)

print(f"Target IP      : {target}")
print(f"Ports Scanned  : {start_port}-{end_port}")
print(f"Open Ports     : {len(open_ports)}")
print(f"Start Time     : {start_time}")
print(f"End Time       : {end_time}")
print(f"Duration       : {end_time - start_time}")

with open("scan_results.txt", "w") as file:
    file.write(f"Target: {target}\n\n")

    for port, service in open_ports:
        file.write(f"Port {port} OPEN ({service})\n")

print("\nResults saved in scan_results.txt")
