import socket
import threading

clients = []

def broadcast(message, sender):
    for client in clients:
        # Skip the sender
        if client != sender:
            try:
                client.send(message)
            except:
                if client in clients:
                    clients.remove(client)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)

            if not message:
                break

            # Send to everyone except sender
            broadcast(message, client)

        except:
            break

    if client in clients:
        clients.remove(client)

    client.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 1235))
    server.listen()

    print("Server started...")

    while True:
        client, addr = server.accept()
        print(f"Connected: {addr}")

        clients.append(client)

        thread = threading.Thread(
            target=handle_client,
            args=(client,),
            daemon=True
        )
        thread.start()

main()