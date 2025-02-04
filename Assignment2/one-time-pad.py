import time


def generatePad(length):
    pad = ""
    while len(pad) < length:
        input("Press a button")
        timi = time.time()
        nmbr = str(timi)[-3:]
        ascii = int(nmbr) % 126
        pad += chr(ascii)
    
    writeFile(pad, "Assignment2/pad.txt")
    return pad
    

def encrypt(plaintext, pad):
    ciphertext = ""

    for i in range(len(plaintext)):
        xorValues = ord(plaintext[i]) ^ ord(pad[i])
        ciphertext += chr(xorValues)

    writeFile(ciphertext, "Assignment2/ciphertext.txt")

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
