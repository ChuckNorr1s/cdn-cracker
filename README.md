# CDN Cracker

CDN Cracker is a script designed to check a list of IP addresses for their association with a specific domain by analyzing the HTML title of their corresponding websites. It utilizes concurrent execution to efficiently process multiple IP addresses simultaneously.

# WARNING

Please note that CDN Cracker is currently in the **early alpha state**, and it may contain bugs or unexpected behavior. Use it at your own risk.

For educational purposes only!

## Prerequisites

- Python 3.x
- Masscan
- Bash
## Installation

1. Clone the repository:

```git clone https://github.com/your-username/cdn-cracker.git```

2. Navigate to the project directory:

```cd cdn-cracker```

3. Install the required dependencies:

```chmod +x setup.sh && ./setup.sh```

## Usage

```python3 cdn-cracker.py [target_title] [file_path] [domain]```

Arguments:
- `target_title`: The target HTML title to search for
- `file_path`: The file path to save the results
- `domain`: The domain name to modify the Host header

### To get a list of IPs

```python3 get-ips.py [network_range]```

Replace [network_range] with the desired IP range to scan. For example:

```python3 get-ips.py 192.168.0.0/24```

The script will use `masscan` to scan the specified IP range for open ports (80 and 443) and generate the results in a `ips.txt` file.

## Important Notes

- Disable SSL warnings: The script disables SSL warnings to allow connections to websites with invalid or self-signed certificates. Use caution and ensure the target websites are trusted.
- IP Address File: The script reads IP addresses from a file named `ips.txt`. Make sure to provide the file with the desired IP addresses to check.
- Maximum Threads: The maximum number of concurrent threads for execution is set to 100 by default. Adjust this value (`num_threads`) based on your system's capabilities and network conditions.

## Example

To check if the HTML title of each IP address's corresponding website contains the target title "Example Domain" and save the results to a file named `results.txt`:

```python3 cdn-cracker.py "Example Domain" results.txt example.com```

## Progress and Timing

The script provides progress updates during execution, indicating the percentage of completed IP addresses and the elapsed and remaining time. The timing format is displayed in hours, minutes, and seconds.

## Bugs and Issues

CDN Cracker is in the early alpha stage, and it may contain bugs or issues. If you encounter any problems or have suggestions for improvement, please open an issue on the GitHub repository.

## Contribution

CDN Cracker is an open-source project, and contributions are welcome. If you have any suggestions, bug fixes, or improvements, please feel free to submit a pull request.

