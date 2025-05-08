import socket
import requests
import whois as pywhois
import json

# פונקציה לבדיקת זמינות אתר
def check_site_availability(url):
    try:
        response = requests.get(url, timeout=5)
        return f"[+] Site is up! Status Code: {response.status_code}"
    except requests.exceptions.RequestException:
        return "[-] Site is down or unreachable."

# פונקציה לסריקת פורטים פתוחים
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

# פונקציה לאחזור מידע WHOIS על דומיין
def domain_info(domain):
    try:
        info = pywhois.whois(domain)
        return json.dumps(info, indent=4)
    except Exception as e:
        return f"[-] WHOIS lookup failed: {str(e)}"

# פונקציה עזר להדפיס את הדוח
def print_report(url, host):
    print("\n[*] Report for", url)
    print(check_site_availability(url))
    print("Open Ports:", scan_ports(host))
    print("WHOIS Info:\n", domain_info(host))

# דוגמה לשימוש
if __name__ == "__main__":
    url = input("Enter the URL (e.g. https://example.com): ")
    
    # אם לא הוזן פרוטוקול, מוסיפים https://
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
    
    host = url.split("//")[-1]
    
    print_report(url, host)
