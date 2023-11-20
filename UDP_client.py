# Smit Padshala
# 21BCP187
import socket

def start_udp_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("UDP Client is ready to send messages. Type 'exit' to quit.")

    while True:
        message = input("Enter a message to send to the server: ")
        client_socket.sendto(message.encode(), (host, port))

        if message.lower() == "exit":
            break

        data, server_address = client_socket.recvfrom(1024)
        print(f"Received from server: {data.decode()}")
            
    if data.decode() == "exit":
        client_socket.close()

if __name__ == "__main__":
    host = 'localhost'
    port = 12345
    start_udp_client(host, port)