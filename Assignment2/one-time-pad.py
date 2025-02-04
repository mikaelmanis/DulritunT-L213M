import time
import random
import bitarray

def generatePad(length):
    pad = ""
    while len(pad) < length:
        input("Press a button")
        timi = time.time()
        nmbr = str(timi)[-3:]
        ascii = int(nmbr) % 126
        pad += chr(ascii)
    ba = bitarray.bitarray()
    ba.frombytes(pad.encode("utf-8"))
    writeFile(str(ba), "Assignment2/pad.txt")
    return pad

# Generates the pad using the random library
def generatePadOS(length):
    pad = ""
    while len(pad) < length:
        pad += chr(random.randint(0, 126))

    writeFile(pad, "Assignment2/pad.txt")
    return pad

def encrypt(plaintext, pad):
    ciphertext = ""

    for i in range(len(plaintext)):
        xorValues = ord(plaintext[i]) ^ ord(pad[i])
        ciphertext += chr(xorValues)

    ba = bitarray.bitarray()
    ba.frombytes(ciphertext.encode("utf-8"))
    writeFile(str(ba), "Assignment2/ciphertext.txt")
    return ciphertext
    
def decrypt(ciphertext, pad):
    plaintext = ""

    for i in range(len(ciphertext)):
        xorValues = ord(ciphertext[i]) ^ ord(pad[i])
        plaintext += chr(xorValues)

    writeFile(plaintext, "Assignment2/decrypted.txt")
    return plaintext

def writeFile(text, path):
    with open(path, "w") as file:
        file.write(text)

def main():
    plaintext = open("Assignment2/text.txt").read()
    textLength = len(plaintext)
    pad = generatePad(textLength)
    ciphertext = encrypt(plaintext, pad)
    decrypted = decrypt(ciphertext, pad)
    
if __name__ == "__main__":
    main()
