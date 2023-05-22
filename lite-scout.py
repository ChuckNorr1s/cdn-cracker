import os
import sys
import requests

def get_shodan_results(query, api_key):
    url = f"https://api.shodan.io/shodan/host/search?key={api_key}&query={query}"
    response = requests.get(url)
    data = response.json()
    ips = [result['ip_str'] for result in data['matches']]
    return ips

def save_to_file(ips):
    with open("ips.txt", "w") as file:
        for ip in ips:
            file.write(ip + "\n")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <query>")
        return

    query = sys.argv[1]

    shodan_api_key = os.getenv("SHODAN_API_KEY")

    if not shodan_api_key:
        print("Please set the environment variable: SHODAN_API_KEY")
        return

    shodan_ips = get_shodan_results(query, shodan_api_key)

    ips = shodan_ips

    save_to_file(ips)
    print(f"Results saved to ips.txt")

if __name__ == "__main__":
    main()
