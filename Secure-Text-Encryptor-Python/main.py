import os
os.system("pip install pycryptodome")

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

# Message
plaintext = "Hello Codec Technologies! This is a secure message."

print("Original Message:")
print(plaintext)

# Generate 256-bit AES Key
key = get_random_bytes(32)

print("\nAES Key (Hex):")
print(key.hex())

# Create Cipher
cipher = AES.new(key, AES.MODE_CBC)

# Encrypt
ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))

encrypted = base64.b64encode(cipher.iv + ciphertext).decode()

print("\nEncrypted Text:")
print(encrypted)

# -------------------
# Decryption
# -------------------

data = base64.b64decode(encrypted)

iv = data[:16]
ciphertext = data[16:]

cipher = AES.new(key, AES.MODE_CBC, iv)

decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)

print("\nDecrypted Message:")
print(decrypted.decode())



from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Generate Keys
key = RSA.generate(2048)

private_key = key
public_key = key.publickey()

message = "This is RSA Encryption Demo"

print("Original Message:")
print(message)

# Encryption
cipher = PKCS1_OAEP.new(public_key)

encrypted = cipher.encrypt(message.encode())

print("\nEncrypted (Base64):")
print(base64.b64encode(encrypted).decode())

# Decryption
cipher = PKCS1_OAEP.new(private_key)

decrypted = cipher.decrypt(encrypted)

print("\nDecrypted Message:")
print(decrypted.decode())



import hashlib

message = "Cyber Security Project"

print("Original Message:")
print(message)

sha = hashlib.sha256()

sha.update(message.encode())

hash_value = sha.hexdigest()

print("\nSHA-256 Hash:")
print(hash_value)
