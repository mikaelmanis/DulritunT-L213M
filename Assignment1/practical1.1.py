alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Encrypts a text using a Caesar cipher
def encrypt(msg, key, alphabet):
    msg = msg.replace(" ", "").upper()
    encryptedMsg = ""
    for i in range(len(msg)):
        if msg[i] in alphabet:
            encryptedMsg += alphabet[(alphabet.index(msg[i]) + key) % len(alphabet)]
        else:
            encryptedMsg += msg[i]
    return encryptedMsg

# Decrypts a text using a Caesar cipher
def decrypt(msg, key, alphabet):
    msg = msg.replace(" ", "").upper()
    decryptedMsg = ""
    for i in range(len(msg)):
        if msg[i] in alphabet:
            decryptedMsg += alphabet[(alphabet.index(msg[i]) - key) % len(alphabet)]
        else:
            decryptedMsg += msg[i]
    return decryptedMsg

# Bruteforces a text which has been encrypted by a Caesar cipher
def bruteForce(msg, alphabet):
    for key in range(len(alphabet)):
        print("Key: " + str(key) + " - " + decrypt(msg, key, alphabet))
        
# Main function which prompts the user to encrypt, decrypt or brute force a file    
def main():
    toDo = input("Would you like to encrypt, decrypt or brute force a file? (e/d/b): ")
    # Chooses the function based on the user input
    match toDo:
        # Encrypts a text
        case "e":
            msg = input("Enter the message you would like to encrypt: ")
            key = int(input("Enter the key you would like to use: "))
            print("Encrypted message: " + encrypt(msg, key, alphabet))
        # Decrypts a text
        case "d":
            msg = input("Enter the message you would like to decrypt: ")
            key = int(input("Enter the key you would like to use: "))
            print("Decrypted message: " + decrypt(msg, key, alphabet))
        # Bruteforces a text
        case "b":
            msg = input("Enter the message you would like to brute force: ")
            bruteForce(msg, alphabet)
        
if __name__ == "__main__":
    main()