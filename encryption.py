from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

key = b'1234567890123456'

def pad(msg):
    return msg + " " * (16 - len(msg) % 16)

def encrypt(message):
    cipher = AES.new(key, AES.MODE_ECB)
    padded = pad(message)
    encrypted = cipher.encrypt(padded.encode())
    return base64.b64encode(encrypted).decode()

def decrypt(cipher_text):
    cipher = AES.new(key, AES.MODE_ECB)
    decoded = base64.b64decode(cipher_text)
    decrypted = cipher.decrypt(decoded).decode()
    return decrypted.strip()