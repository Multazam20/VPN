import socket
import threading
import ipaddress

def handle_client(client_socket, addr):
    print(f"[+] Connection from {addr}")
    while True:
        try:
            data = client_socket.recv(4096)
            if not data:
                break
            print(f"From {addr}: {data.decode()}")
            client_socket.sendall(b"Data received at server.")
        except:
            break
    client_socket.close()

def main():
    host = "0.0.0.0"
    port = 5555

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print(f"[*] Listening on {host}:{port}")
    while True:
        client, addr = server.accept()
        threading.Thread(target=handle_client, args=(client, addr)).start()

if __name__ == "__main__":
    main()
