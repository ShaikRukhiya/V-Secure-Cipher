def encrypt(text, key):
    text = text.upper().replace(" ", "")
    
    # Layer 1: Key-based shifting
    layer1 = ""
    for char in text:
        shifted = chr((ord(char) - 65 + key) % 26 + 65)
        layer1 += shifted

    # Layer 2: Position-based shifting
    layer2 = ""
    for i in range(len(layer1)):
        shifted = chr((ord(layer1[i]) - 65 + key + i) % 26 + 65)
        layer2 += shifted

    # Layer 3: Split, swap, reverse
    mid = len(layer2) // 2
    swapped = layer2[mid:] + layer2[:mid]
    cipher = swapped[::-1]

    return cipher


def decrypt(cipher, key):
    # Reverse Layer 3
    reversed_text = cipher[::-1]
    mid = len(reversed_text) // 2
    swapped_back = reversed_text[mid:] + reversed_text[:mid]

    # Reverse Layer 2
    layer1 = ""
    for i in range(len(swapped_back)):
        shifted = chr((ord(swapped_back[i]) - 65 - key - i) % 26 + 65)
        layer1 += shifted

    # Reverse Layer 1
    original = ""
    for char in layer1:
        shifted = chr((ord(char) - 65 - key) % 26 + 65)
        original += shifted

    return original


# Example
message = "KNOWLEDGE GROWS WHEN CURIOSITY MEETS CONSISTENT EFFORT"
key = 4

encrypted = encrypt(message, key)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted:", decrypted)