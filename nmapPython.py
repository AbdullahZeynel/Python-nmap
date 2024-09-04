import os
import nmap
import ipaddress

# Initialize the nmap.PortScanner object
nm = nmap.PortScanner()

# Screens
main_menu = """
************************************************************************
** Python Nmap Tool **
************************************************************************

Please select an option:

1. IP Scanner
2. Security Vulnerability Scanner
3. Custom Service Detection Tool
4. Network Health Monitor
5. Exit
"""

scan_menu = """
************************************************************************
** Python Nmap Tool **
************************************************************************

Please select an option:

1. Scan a Single IP
2. Scan an IP Range
3. Scan Specific Ports
4. Exit
"""
#_______________________________________________________

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
#_______________________________________________________

# Scan a single IP address for open ports in the range 1-1024.
def scan_single_ip():
    clearScreen()
    target = input("Enter the IP address to scan: ")
    
    try:
        ipaddress.ip_address(target)
        nm.scan(target, '1-1024')
        print(f"Scan results for {target}:")
        print(nm.csv())
        
    except ValueError as e:
        print(f"Invalid IP address: {e}")
    
    except Exception as e:
        print(f"Error during scan: {e}")
    
    finally:
        input("\nPlease press ENTER to return to Main Menu.")
        mainMenu()
#_______________________________________________________

# Scan a range of IP addresses for open ports in the range 1-1024.
def scan_ip_range():
    clearScreen()
    target = input("Enter the IP range to scan (e.g., 192.168.1.1-192.168.1.10): ")
    
    try:
        ip_range = target.split('-')
        if len(ip_range) != 2:
            raise ValueError("IP range must be in the format startIP-endIP")
        
        start_ip, end_ip = ip_range
        ipaddress.ip_address(start_ip)
        ipaddress.ip_address(end_ip)
        
        nm.scan(target, '1-1024')
        print(f"Scan results for IP range {target}:")
        print(nm.csv())
        
    except ValueError as e:
        print(f"Invalid IP address or range: {e}")
    
    except Exception as e:
        print(f"Error during scan: {e}")
    
    finally:
        input("\nPlease press ENTER to return to Main Menu.")
        mainMenu()
#_______________________________________________________

# Scan a specific IP address for specified ports.
def scan_specific_ports():
    clearScreen()
    target = input("Enter the IP address to scan: ")
    ports = input("Enter the ports to scan (e.g., 22, 80, 443): ")
    
    try:
        ipaddress.ip_address(target)
        ports_list = ports.split(',')
        if not all(port.strip().isdigit() for port in ports_list):
            raise ValueError("Ports must be numeric and separated by commas")
        
        nm.scan(target, ports)
        print(f"Scan results for {target} on ports {ports}:")
        print(nm.csv())
        
    except ValueError as e:
        print(f"Invalid IP address or ports: {e}")
    
    except Exception as e:
        print(f"Error during scan: {e}")
    
    finally:
        input("\nPlease press ENTER to return to Main Menu.")
        mainMenu()
#_______________________________________________________

# Scan a specific IP address for vulnerabilities.
def security_vulnerability_scanner():
    clearScreen()
    target = input("Enter the IP address to scan for vulnerabilities: ")
    
    try:
        ipaddress.ip_address(target)
        nm.scan(target, arguments='--script vuln')
        print(f"Vulnerability scan results for {target}:")
        print(nm.csv())
        
    except ValueError as e:
        print(f"Invalid IP address: {e}")
    
    except Exception as e:
        print(f"Error during scan: {e}")
    
    finally:
        input("\nPlease press ENTER to return to Main Menu.")
        mainMenu()
#_______________________________________________________

# Monitor network health for a range of IP addresses.
def network_health_monitor():
    clearScreen()
    target = input("Enter the IP range to monitor network health (e.g., 192.168.1.1-192.168.1.10): ")
    
    try:
        ip_range = target.split('-')
        if len(ip_range) != 2:
            raise ValueError("IP range must be in the format startIP-endIP")
        
        start_ip, end_ip = ip_range
        ipaddress.ip_address(start_ip)
        ipaddress.ip_address(end_ip)
        
        nm.scan(target, arguments='--script network-health')
        print(f"Network health results for {target}:")
        print(nm.csv())
        
    except ValueError as e:
        print(f"Invalid IP address or range: {e}")
    
    except Exception as e:
        print(f"Error during scan: {e}")
    
    finally:
        input("\nPlease press ENTER to return to Main Menu.")
        mainMenu()
#_______________________________________________________

# Detect custom services on a specific IP address.
def custom_service_detection_tool():
    clearScreen()
    target = input("Enter the IP address to detect services: ")
    services = input("Enter the services to detect (comma-separated, e.g., http, ftp): ")
    
    try:
        ipaddress.ip_address(target)
        services_list = services.split(',')
        if not all(service.strip() for service in services_list):
            raise ValueError("Services list cannot be empty and must be comma-separated.")
        
        for service in services_list:
            nm.scan(target, arguments=f'--script {service.strip()}')
        
        print(f"Service detection results for {target}:")
        print(nm.csv())
        
    except ValueError as e:
        print(f"Invalid IP address or service format: {e}")
    
    except Exception as e:
        print(f"Error during scan: {e}")
    
    finally:
        input("\nPlease press ENTER to return to Main Menu.")
        mainMenu()
#_______________________________________________________

def scanMenu():
    clearScreen()
    print(scan_menu)
    choice = input("\nEnter your choice: ")

    match choice:
        case '1':
            scan_single_ip()
        case '2':
            scan_ip_range()
        case '3':
            scan_specific_ports()
        case '4':
            return
        case _:
            input("ERROR: Invalid input.\nPlease press ENTER to continue.")
            scanMenu()
#_______________________________________________________

def mainMenu():
    clearScreen()
    print(main_menu)
    choice = input("\nEnter your choice: ")

    match choice:
        case '1':
            scanMenu()
        case '2':
            security_vulnerability_scanner()
        case '3':
            custom_service_detection_tool()
        case '4':
            network_health_monitor()
        case '5':
            exit()
        case _:
            input("ERROR: Invalid input.\nPlease press ENTER to continue.")
            mainMenu()
#_______________________________________________________

if __name__ == "__main__":
    mainMenu()
