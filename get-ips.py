import subprocess
import sys

# Check if network range is provided
if len(sys.argv) < 2:
    print("Please provide the network range to scan in CIDR format (example : 18.0.0.0/8 ) .")
    print("Usage: python3 masscan_script.py [network_range]")
    sys.exit(1)

# Get the network range from command-line argument
network_range = sys.argv[1]

# Run masscan to scan for open ports on the target IP range
command = f"sudo masscan -p80,443 --range {network_range} --rate=1000 --banners --max-rate 10000 --script=banner --wait 0 -oG ips.txt"
subprocess.run(command, shell=True)
