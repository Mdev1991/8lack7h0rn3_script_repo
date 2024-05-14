import socket
import threading

def check_port(host, port):
    try:
        # Create a socket object
        check_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        check_socket.settimeout(1)  # Set a timeout for connection attempts
        
        # Attempt to connect to the host and port
        result = check_socket.connect_ex((host, port))
        
        # Check if the port is open
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        
        # Close the socket
        check_socket.close()
    except Exception as e:
        print(f"Error checking port {port}: {e}")

def scan_ports(host, start_port, end_port):
    print(f"Scanning ports on {host}...\n")
    for port in range(start_port, end_port + 1):
        # Create a new thread to check each port
        threading.Thread(target=check_port, args=(host, port)).start()

if __name__ == "__main__":
    host = "IP"  # localhost
    start_port = 1
    end_port = 600  # You can adjust this range as needed
    
    scan_ports(host, start_port, end_port)