file = input("What file would you like to open? ")
text = open(file, "r").read()
frequency = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}
for line in text:
    line = line.replace("\n", "")
    line = line.replace(" ", "").upper()
    for letter in line:
        if letter in frequency:
            frequency[letter] += 1
            
for letter in frequency:
    print(letter + ": " + str(frequency[letter]))
    