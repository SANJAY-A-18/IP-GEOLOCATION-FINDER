import requests
import os
from dotenv import load_dotenv

# Load token from .env file
load_dotenv()
TOKEN = os.getenv("IPINFO_TOKEN")

def get_ip_info(ip_address):
    url = f"https://ipinfo.io/{ip_address}?token={TOKEN}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"\nIP Address: {data.get('ip')}")
        print(f"City: {data.get('city')}")
        print(f"Region: {data.get('region')}")
        print(f"Country: {data.get('country')}")
        print(f"Location (Lat,Long): {data.get('loc')}")
        print(f"ISP: {data.get('org')}")
        print(f"Timezone: {data.get('timezone')}")
    else:
        print("❌ Failed to fetch data. Check IP address or token.")

def get_my_public_ip():
    try:
        response = requests.get("https://ipinfo.io/json")
        if response.status_code == 200:
            return response.json().get("ip")
    except:
        print("❌ Could not fetch public IP.")
    return None

# Main Program
while True:
    ip = input("\nEnter an IP address (leave blank to auto-detect your public IP, or type 'exit' to quit): ").strip()
    if ip.lower() == 'exit':
        break
    elif ip == "":
        ip = get_my_public_ip()
        if not ip:
            print("❌ Unable to retrieve your public IP.")
            continue
    get_ip_info(ip)
