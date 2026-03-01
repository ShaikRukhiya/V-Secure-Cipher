# V-Secure Cipher 🔐

## Project Overview


The objective of this project is to design and implement a custom cryptographic algorithm called **V-Secure Cipher** that performs encryption and decryption using multiple security layers.

---

## Algorithm Concept

The V-Secure Cipher combines multiple cryptographic techniques:

1. Key-based character shifting
2. Position-based shifting
3. Split and swap transposition
4. Reverse transformation

These layers increase complexity and make decoding difficult without knowing the algorithm and key.

---

## Encryption Process

1. Convert text to uppercase.
2. Apply key-based shifting.
3. Apply position-based shifting.
4. Split the text into two halves.
5. Swap halves.
6. Reverse the final string.

---

## Decryption Process

The decryption process reverses all encryption steps:

1. Reverse string
2. Swap halves back
3. Reverse position-based shifting
4. Reverse key-based shifting

---

## Technologies Used

- Python
- VS Code
- Git & GitHub

---

## How to Run the Project

1. Open project in VS Code.
2. Run the Python file:

```bash
python v_secure_cipher.py
