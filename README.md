# Secure Cryptography Suite (AES, RSA & SHA-256)

A comprehensive Python script demonstrating the implementation of symmetric encryption, asymmetric encryption, and cryptographic hashing using the **PyCryptodome** library.

## Features & Code Structure

The project implements three distinct security mechanisms sequentially in a single execution flow:

1. **AES-256 (Symmetric Encryption):** 
   * Uses AES in **CBC mode**.
   * Generates a random 256-bit key.
   * Handles text padding (`pad`/`unpad`) and prepends the Initialization Vector (IV) before Base64 encoding.

2. **RSA-2048 (Asymmetric Encryption):**
   * Generates a 2048-bit key pair.
   * Encrypts the plaintext using the **Public Key** with **PKCS1_OAEP** padding.
   * Decrypts the ciphertext back using the corresponding **Private Key**.

3. **SHA-256 (Cryptographic Hashing):**
   * Generates a secure, fixed-length 256-bit one-way hash of a target message to ensure data integrity.

## Prerequisites

To run your code, you need Python installed along with the `pycryptodome` library.

Install the required package via pip:
```bash
pip install pycryptodome
```

## Code Execution

Save your exact code inside a file named `main.py` and run it using:
```bash
python main.py
```

## Expected Output Format

When executed successfully, the terminal will display the output in the following sequence:

```text
Original Message:
Hello Codec Technologies! This is a secure message.

AES Key (Hex):
[Generated 64-character Hex String]

Encrypted Text:
[Base64 Encoded AES Ciphertext String]

Decrypted Message:
Hello Codec Technologies! This is a secure message.

Original Message:
This is RSA Encryption Demo

Encrypted (Base64):
[Base64 Encoded RSA Ciphertext String]

Decrypted Message:
This is RSA Encryption Demo

Original Message:
Cyber Security Project

SHA-256 Hash:
[Generated 64-character SHA-256 Hash String]
```

## Internship Context
This project was compiled and tested as part of the hands-on technical assessment for the Cybersecurity Internship at **Codec Technologies**.
