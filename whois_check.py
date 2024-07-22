import whois
import sys

def check_domain(domain):
    try:
        w = whois.whois(domain)
        expiration_date = w.expiration_date
        status = w.status
        print(f"Expiration Date: {expiration_date}")
        print(f"Status: {status}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: whois_check.py <domain>")
        sys.exit(1)
    domain = sys.argv[1]
    check_domain(domain)
