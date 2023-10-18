from Crypto.Cipher import AES
import base64

BLOCK_SIZE = 32

PADDING = '{'

# Encrypted text to decrypt
encrypted = "xpd4OA7GZYDfn4lTMJW/EEqgp26BlgjxsTonc1Elcgo="

def decode_aes(c, e):
    return c.decrypt(base64.b64decode(e)).decode('latin-1').rstrip(PADDING)

with open('words111.txt') as f:
    words = f.read().split('\n')

for secret in words:
    if secret[-1:] == "\n":
        print("Error, new line character at the end of the string. This will not match!")
    elif len(secret.encode('latin-1')) >= 32:
        print("Error, string too long. Must be less than 32 bytes.")
    else:
        cipher = AES.new(str(secret + (BLOCK_SIZE - len(secret.encode('latin-1')) % BLOCK_SIZE) * PADDING).encode('latin-1'), AES.MODE_ECB)

        # decode the encoded string
        decoded = decode_aes(cipher, encrypted)

        if decoded != '':
            print('Decoded: '+decoded+"\n")