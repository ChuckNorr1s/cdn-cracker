import subprocess
import sys
import re

# Check if network range is provided
if len(sys.argv) < 2:
    print("Please provide the network range to scan in CIDR format (example : 18.0.0.0/8 ) .")
    print("Usage: python3 masscan_script.py [network_range]")
    sys.exit(1)

# Get the network range from command-line argument
network_range = sys.argv[1]

# Run masscan to scan for open ports on the target IP range
command = f"sudo masscan -p80,443 --range {network_range} --rate=1000 --banners --max-rate 10000 --wait 0 -oG ips.txt && sudo chmod 777 ips.txt"
subprocess.run(command, shell=True)

print("...rewritting in right format...")
# Read the contents of ips.txt
with open('ips.txt', 'r') as file:
    content = file.read()

# Use regular expressions to extract the IP addresses
ip_addresses = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', content)

# Write the extracted IP addresses to ips.txt
with open('ips.txt', 'w') as file:
    for ip in ip_addresses:
        file.write(ip + '\n')
