import string

# Rail Fence Cipher
def rail_fence_encrypt(text, key):
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    dir_down = False
    row, col = 0, 0

    # Fill the rail matrix
    for char in text:
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        rail[row][col] = char
        col += 1
        row += 1 if dir_down else -1

    # Extract the encrypted text
    encrypted_text = ''.join(char for row in rail for char in row if char != '\n')
    return encrypted_text


def rail_fence_decrypt(cipher, key):
    rail = [['\n' for i in range(len(cipher))] for j in range(key)]
    dir_down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        rail[row][col] = '*'
        col += 1
        row += 1 if dir_down else -1

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        if rail[row][col] != '\n':
            result.append(rail[row][col])
            col += 1
        row += 1 if dir_down else -1

    return ''.join(result)

# Vigenère Cipher
def vigenere_encrypt(text, key):
    key = key.upper()
    key_index = 0
    encrypted_text = ''

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)
            key_index = (key_index + 1) % len(key)
        else:
            encrypted_text += char

    return encrypted_text

def vigenere_decrypt(cipher, key):
    key = key.upper()
    key_index = 0
    decrypted_text = ''

    for char in cipher:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - base - shift) % 26 + base)
            key_index = (key_index + 1) % len(key)
        else:
            decrypted_text += char

    return decrypted_text

# Caesar Cipher
def caesar_encrypt(text, shift):
    shift %= 26
    encrypted_text = ''

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted_text += char

    return encrypted_text

def caesar_decrypt(cipher, shift):
    shift %= 26
    decrypted_text = ''

    for char in cipher:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted_text += char

    return decrypted_text

# Combined Encryption and Decryption
def encrypt_text(text, rail_key, vigenere_key, caesar_shift):
    step1 = rail_fence_encrypt(text, rail_key)
    step2 = vigenere_encrypt(step1, vigenere_key)
    step3 = caesar_encrypt(step2, caesar_shift)
    return step3

def decrypt_text(cipher, rail_key, vigenere_key, caesar_shift):
    step1 = caesar_decrypt(cipher, caesar_shift)
    step2 = vigenere_decrypt(step1, vigenere_key)
    step3 = rail_fence_decrypt(step2, rail_key)
    return step3