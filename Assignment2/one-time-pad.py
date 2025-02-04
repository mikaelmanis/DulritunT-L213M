"""fileIn = open("Assignment2/image.png", "rb")
fileOut = open("Assignment2/newImage.png", "wb")

inBytes = fileIn.read()
fileOut.write(inBytes)

fileOut.close()"""

from bitarray import bitarray
import math


text = open("Assignment1/book.txt", "r").read()
frequency = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}
for line in text:
    line = line.replace("\n", "")
    line = line.replace(" ", "").upper()
    for letter in line:
        if letter in frequency:
            frequency[letter] += 1

frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))

def probabilityDistribution(freqDist):
    probDist = {}
    total = sum(freqDist.values())
    for key in freqDist:
        probDist[key] = freqDist[key] / total
    return probDist

def entropy(probDist, base):
    entropy = 0
    for key in probDist:
        entropy -= probDist[key] * math.log(probDist[key], base)
    return entropy

print(entropy(probabilityDistribution(frequency), 1114111))
ba = bitarray.bitarray()
bookInBinary = ba.frombytes(text.encode("utf-8")).tolist()

print(entropy(probabilityDistribution(bookInBinary,base=2)))