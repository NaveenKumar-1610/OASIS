#Project Title : Browser-Based Chat Application

import socket
import threading

def server_handler(client_socket, client_address):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break

            print(f"Received from {client_address}: {message}")

            response = input("Your response: ")
            client_socket.send(response.encode("utf-8"))
        except ConnectionResetError:
            break

    print(f"Connection closed: {client_address}")
    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9999))
server_socket.listen(5)
print("Server is listening...")

while True:
    client_socket, client_address = server_s…

#clint side code
#this client code should be run in different system

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9999))

while True:
    message = input("Your message: ")
    client_socket.send(message.encode("utf-8"))

    response = client_socket.recv(1024).decode("utf-8")
    print(f"Received from server: {response}")
