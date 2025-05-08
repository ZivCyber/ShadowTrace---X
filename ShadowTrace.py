import socket
import requests
import whois

# פונקציה לבדוק את מצב האתר (לראות אם הוא פעיל או לא)
def check_website_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Website {url} is up and running!")
        else:
            print(f"Website {url} returned status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error checking {url}: {e}")

# פונקציה לביצוע סריקת פורטים
def scan_ports(target_ip, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    if open_ports:
        print(f"Open ports on {target_ip}: {', '.join(map(str, open_ports))}")
    else:
        print(f"No open ports found on {target_ip}.")

# פונקציה לקבלת מידע על דומיין
def get_domain_info(domain):
    try:
        domain_info = whois.whois(domain)
        print(f"Domain info for {domain}: {domain_info}")
    except Exception as e:
        print(f"Error retrieving domain info for {domain}: {e}")

if __name__ == "__main__":
    # דוגמה לשימוש:
    url = "https://www.example.com"
    check_website_status(url)

    ip = "93.184.216.34"  # דוגמת IP (של example.com)
    ports = [80, 443, 8080]
    scan_ports(ip, ports)

    domain = "example.com"
    get_domain_info(domain)
