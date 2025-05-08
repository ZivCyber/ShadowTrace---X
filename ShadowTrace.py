import socket
import requests
import whois
import json

def check_site_availability(url):
    try:
        response = requests.get(url, timeout=5)
        return f"[+] Site is up! Status Code: {response.status_code}"
    except requests.exceptions.RequestException:
        return "[-] Site is down or unreachable."

def scan_ports(host):
    print(f"[*] Scanning ports on {host}...")
    common_ports = [21, 22, 23, 80, 443, 8080]
    open_ports = []
    for port in common_ports:
        sock = socket.socket()
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def domain_info(domain):
    try:
        info = whois.whois(domain)
        return json.dumps(info, indent=4)
    except Exception as e:
        return f"[-] WHOIS lookup failed: {str(e)}"

def print_report(url, host):
    print("\n[*] Report for", url)
    print(check_site_availability(url))
    print("Open Ports:", scan_ports(host))
    print("WHOIS Info:\n", domain_info(host))

if __name__ == "__main__":
    url = input("Enter a website URL (like https://github.com): ").strip()
    if not url.startswith("http"):
        url = "https://" + url
    host = url.split("//")[-1].split("/")[0]
    print_report(url, host)
