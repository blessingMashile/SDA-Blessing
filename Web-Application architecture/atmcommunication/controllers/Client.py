# client.py
import socket

HOST = '127.0.0.1'
PORT = 65432

# Send health request
# Send authorization request
# Send reversal request
# Send host total request
# Send configuration request -> change banks/ server config in DB

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        # Send health request
        s.sendall(b'health')
        data = s.recv(1024)
        print('Health:', data.decode())
        
        # Send configuration request
        s.sendall(b'configuration')
        data = s.recv(1024)
        print('Configuration:', data.decode())

if __name__ == "__main__":
    main()
