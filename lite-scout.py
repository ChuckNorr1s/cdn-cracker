import os
import sys
import requests

def get_shodan_results(query, api_key):
    url = f"https://api.shodan.io/shodan/host/search?key={api_key}&query={query}"
    response = requests.get(url)
    data = response.json()
    ips = [result['ip_str'] for result in data['matches']]
    return ips

def get_censys_results(query, api_id, api_secret):
    url = "https://search.censys.io/api/v1/search/ipv4"
    data = {
        "query": query,
        "apikey": api_id,
        "secret": api_secret
    }
    response = requests.post(url, json=data)
    data = response.json()
    ips = [result['ip'] for result in data['results']]
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
    censys_api_id = os.getenv("CENSYS_API_ID")
    censys_api_secret = os.getenv("CENSYS_API_SECRET")

    if not shodan_api_key or not censys_api_id or not censys_api_secret:
        print("Please set the environment variables: SHODAN_API_KEY, CENSYS_API_ID, CENSYS_API_SECRET")
        return

    shodan_ips = get_shodan_results(query, shodan_api_key)
    censys_ips = get_censys_results(query, censys_api_id, censys_api_secret)

    ips = shodan_ips + censys_ips

    save_to_file(ips)
    print(f"Results saved to ips.txt")

if __name__ == "__main__":
    main()
