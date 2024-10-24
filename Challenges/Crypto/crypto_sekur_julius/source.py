from random import choices
import os

def julius_decrypt(ct, shift):
    msg = ''
    for c in ct:
        if c == '0':
            msg += ' '
        elif not ord('A') <= ord(c) <= ord('Z'):
            msg += c
        else:
            o = ord(c) - 65
            msg += chr(65 + (o - shift) % 26)
    return msg

def decrypt(ct, key):
    for shift in reversed(key):
        ct = julius_decrypt(ct, shift)
    return ct

def brute_force_decrypt(ct):
    for key_length in range(1, 1338):  # Try all possible key lengths
        for _ in range(100):  # Try multiple random keys for each length
            key = os.urandom(key_length)
            decrypted = decrypt(ct, key)
            if 'FLAG' in decrypted:  # Assuming the flag contains 'FLAG'
                return decrypted
    return "Decryption failed"

with open('output.txt', 'r') as f:
    encrypted_msg = f.read()

decrypted_msg = brute_force_decrypt(encrypted_msg)
print(decrypted_msg)
