import socket
import threading

clients = []

def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            clients.remove(client)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            clients.remove(client)
            client.close()
            break

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 1235))
    server.listen()

    print("Server started...")

    while True:
        client, addr = server.accept()
        print(f"Connected: {addr}")

        clients.append(client)

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

main()