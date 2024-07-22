import dns.resolver
import sys

def check_dns(domain, record_type):
    try:
        result = dns.resolver.resolve(domain, record_type)
        for val in result:
            print(f"{record_type}: {val.to_text()}")
    except dns.resolver.NoAnswer:
        print(f"No {record_type} record found for {domain}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: dns_check.py <domain> <record_type>")
        sys.exit(1)
    domain = sys.argv[1]
    record_type = sys.argv[2]
    check_dns(domain, record_type)
