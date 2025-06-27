# Simple TCP Port Scanner (Python)

A lightweight multithreaded TCP port scanner built in Python. This tool scans a range of ports on a given IP address or domain and identifies which ports are open. Designed for ethical testing, educational use, and networking practice.

---

##  Features

- Scan any host (IP or domain name)
- Custom port range support (e.g. `20-1000`)
- Multithreaded scanning using `threading`
- Timeout handling for unreachable hosts
- No external dependencies (pure Python standard library)

---

##  Technologies Used

- Python 3
- Libraries: `socket`, `threading`, `argparse`

---

## Example Usage

```bash
# Scan default range (1–1024)
python port_scanner.py 192.168.1.1

# Scan custom range
python port_scanner.py scanme.nmap.org -p 20-100
