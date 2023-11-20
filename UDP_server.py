# Smit Padshala
# 21BCP187
import socket

def start_udp_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"UDP Server listening on {host}:{port}")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        print(f"Received data from {client_address}: {data.decode()}")

        response = input("Enter your response (or type 'exit' to quit): ")
        if response.lower() == "exit":
            server_socket.sendto(response.encode(), client_address)
            break

        server_socket.sendto(response.encode(), client_address)

    # response = input("Server wants to quit give your response (or type 'exit' to quit): ")
    # if response.lower() == "exit":
    server_socket.close()

if __name__ == "__main__":
    host = 'localhost'
    port = 12345
    start_udp_server(host, port)
