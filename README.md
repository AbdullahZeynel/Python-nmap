# Python Nmap Tool

## Overview

The Python Nmap Tool is a command-line utility designed for educational purposes to demonstrate how to interact with `nmap` using Python. By utilizing the `python-nmap` library, this tool allows users to perform various network scans to identify open ports, detect vulnerabilities, and monitor network health. This README will guide you through the installation, usage, and functionality of the tool.

## Features

- **IP Scanner**: Scan individual IP addresses or ranges for open ports.
- **Security Vulnerability Scanner**: Identify potential security vulnerabilities on a specified IP address.
- **Custom Service Detection Tool**: Detect specific services running on an IP address.
- **Network Health Monitor**: Evaluate the health of a network by scanning an IP range.

## Installation

To get started with the Python Nmap Tool, follow these steps:

1. **Clone the Repository**

   Clone the repository to your local machine using Git:

   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

2. **Create and Activate a Virtual Environment**

   It is highly recommended to use a virtual environment to manage dependencies:

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
   ```

3. **Install Required Packages**

   Install the necessary Python packages listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the Python Nmap Tool, follow these instructions:

1. **Run the Tool**

   Execute the tool using Python:

   ```bash
   python nmapPython.py
   ```

2. **Main Menu Options**

   After running the tool, you will be presented with the main menu. Here’s a breakdown of each option:

   - **IP Scanner**: This option allows you to scan for open ports on a single IP address, an IP range, or specific ports.
   - **Security Vulnerability Scanner**: Use this to check for known security vulnerabilities on an IP address.
   - **Custom Service Detection Tool**: Detect and report on specific services running on an IP address.
   - **Network Health Monitor**: Assess the health of a network by scanning a range of IP addresses.

### Detailed Usage

1. **Scan a Single IP Address**

   - **Prompt**: Enter the IP address to scan.
   - **Description**: Scans ports 1-1024 on the specified IP address. This is useful for identifying which ports are open and potentially vulnerable on a single machine.

   ```plaintext
   Enter the IP address to scan: 192.168.1.1
   ```

2. **Scan an IP Range**

   - **Prompt**: Enter the IP range in the format `startIP-endIP`.
   - **Description**: Scans all IP addresses within the specified range for open ports. This can help in identifying vulnerabilities across a subnet.

   ```plaintext
   Enter the IP range to scan (e.g., 192.168.1.1-192.168.1.10): 192.168.1.1-192.168.1.10
   ```

3. **Scan Specific Ports**

   - **Prompt**: Enter the IP address and the ports to scan.
   - **Description**: Scans specific ports on the given IP address. Useful for targeting particular services or vulnerabilities.

   ```plaintext
   Enter the IP address to scan: 192.168.1.1
   Enter the ports to scan (e.g., 22, 80, 443): 22,80,443
   ```

4. **Security Vulnerability Scan**

   - **Prompt**: Enter the IP address to scan for vulnerabilities.
   - **Description**: Uses `nmap`'s vulnerability scanning scripts to identify known security issues on the IP address.

   ```plaintext
   Enter the IP address to scan for vulnerabilities: 192.168.1.1
   ```

5. **Custom Service Detection**

   - **Prompt**: Enter the IP address and services to detect (comma-separated).
   - **Description**: Detects specified services running on the IP address. The services are identified using `nmap`'s script engine.

   ```plaintext
   Enter the IP address to detect services: 192.168.1.1
   Enter the services to detect (comma-separated, e.g., http, ftp): http,ftp
   ```

6. **Network Health Monitoring**

   - **Prompt**: Enter the IP range to monitor network health.
   - **Description**: Checks the network health of the specified IP range using `nmap`'s network health script.

   ```plaintext
   Enter the IP range to monitor network health (e.g., 192.168.1.1-192.168.1.10): 192.168.1.1-192.168.1.10
   ```

## Notes

- **Permissions**: Ensure you have the appropriate permissions to scan the networks or IP addresses. Unauthorized scanning can be illegal and unethical.
- **Usage**: This tool is intended for educational purposes to help understand `nmap` functionality through Python. Always use it responsibly.
- **Dependencies**: The tool relies on `python-nmap` and `nmap` itself. Make sure `nmap` is installed on your system.
