import socket
import ipaddress

def main():
    host = "127.0.0.1"  # Change to server IP if on LAN
    port = 5555

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print(f"[*] Connected to server at {host}:{port}")

    while True:
        msg = input("Send data: ")
        if msg.lower() == "exit":
            break
        try:
            ip = ipaddress.ip_address(msg)
            print(f"Valid IP entered: {ip}")
        except ValueError:
            print("Not a valid IP, sending raw data...")

        client.sendall(msg.encode())
        data = client.recv(4096)
        print(f"Server replied: {data.decode()}")

    client.close()

if __name__ == "__main__":
    main()
