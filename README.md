```markdown
# Python Nmap Tool

## Overview

The Python Nmap Tool is a command-line utility for network scanning using the `python-nmap` library. It allows users to perform various types of scans, including IP scanning, vulnerability scanning, custom service detection, and network health monitoring. This tool is intended for educational purposes to help users understand how to leverage `nmap` in Python for network analysis.

## Features

- **IP Scanner**: Scan a single IP address or a range of IP addresses for open ports.
- **Security Vulnerability Scanner**: Scan a specific IP address for known security vulnerabilities.
- **Custom Service Detection Tool**: Detect specific services running on an IP address.
- **Network Health Monitor**: Monitor the health of a network by scanning an IP range.

## Requirements

- Python 3.x
- `python-nmap` library

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

2. **Create and Activate a Virtual Environment (Optional but Recommended)**

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. **Install the Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Tool**

   ```bash
   python nmapPython.py
   ```

2. **Select an Option from the Main Menu**

   - **IP Scanner**: Choose this option to scan a single IP address, a range of IP addresses, or specific ports.
   - **Security Vulnerability Scanner**: Use this option to check for vulnerabilities on a specific IP address.
   - **Custom Service Detection Tool**: Detect specific services running on an IP address.
   - **Network Health Monitor**: Monitor the health of a network by scanning an IP range.

### Example Usage

1. **Scan a Single IP Address**

   - Enter an IP address when prompted.
   - The tool will scan ports 1-1024 on the given IP address.

   ```plaintext
   Enter the IP address to scan: 192.168.1.1
   ```

2. **Scan an IP Range**

   - Enter the IP range in the format `startIP-endIP`.

   ```plaintext
   Enter the IP range to scan (e.g., 192.168.1.1-192.168.1.10): 192.168.1.1-192.168.1.10
   ```

3. **Scan Specific Ports**

   - Enter the IP address and the ports to scan.

   ```plaintext
   Enter the IP address to scan: 192.168.1.1
   Enter the ports to scan (e.g., 22, 80, 443): 22,80,443
   ```

4. **Security Vulnerability Scan**

   - Enter the IP address to check for vulnerabilities.

   ```plaintext
   Enter the IP address to scan for vulnerabilities: 192.168.1.1
   ```

5. **Custom Service Detection**

   - Enter the IP address and the services to detect (comma-separated).

   ```plaintext
   Enter the IP address to detect services: 192.168.1.1
   Enter the services to detect (comma-separated, e.g., http, ftp): http,ftp
   ```

6. **Network Health Monitoring**

   - Enter the IP range to monitor network health.

   ```plaintext
   Enter the IP range to monitor network health (e.g., 192.168.1.1-192.168.1.10): 192.168.1.1-192.168.1.10
   ```

## Notes

- Ensure that you have the necessary permissions to scan the networks or IP addresses you are targeting.
- Use this tool responsibly and in compliance with all applicable laws and regulations.
