import socket
import threading
import argparse

# Set timeout for socket connection
socket.setdefaulttimeout(1)

open_ports = []

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
                open_ports.append(port)
    except Exception:
        pass

def main():
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("host", help="Target IP or domain")
    parser.add_argument("-p", "--ports", help="Port range, e.g. 20-1000", default="1-1024")

    args = parser.parse_args()
    host = args.host
    port_range = args.ports

    try:
        target_ip = socket.gethostbyname(host)
        print(f"📡 Scanning target {host} ({target_ip})...\n")
    except socket.gaierror:
        print("❌ Hostname could not be resolved.")
        return

    start, end = map(int, port_range.split("-"))
    threads = []

    for port in range(start, end + 1):
        t = threading.Thread(target=scan_port, args=(host, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n✅ Scan complete.")
    if open_ports:
        print(f"\n🔓 Open ports: {open_ports}")
    else:
        print("🚫 No open ports detected.")

if __name__ == "__main__":
    main()
