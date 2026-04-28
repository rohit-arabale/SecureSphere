import socket
import threading
from encryption import encrypt, decrypt
from spam_filter import is_spam

def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode()
            print("Received:", decrypt(message))
        except:
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 1235))

    threading.Thread(target=receive_messages, args=(client,)).start()

    while True:
        msg = input()

        if is_spam(msg):
            print("Blocked by AI filter!")
            continue

        encrypted = encrypt(msg)
        client.send(encrypted.encode())

main()