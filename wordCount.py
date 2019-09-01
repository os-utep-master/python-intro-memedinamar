import os
import re
import sys

inputFile = sys.argv[1]
outputFile = sys.argv[2]

newFile = open("outText.txt", "w+")
with open(inputFile, "r") as file:
    for line in file:
        for word in re.findall(r'\w+', line):
            newFile.write(word.lower() + '\n')
newFile.close()

dictionary = {}
with open("outText.txt", 'r') as f:
    for line in f:
        ana = line[:-1]
        if ana in dictionary:
            dictionary[ana] = dictionary.get(ana) + 1
        else:
            dictionary[ana] = 1

with open(outputFile, 'w+') as f:
    for key, val in sorted(dictionary.items()):
        print(key, val, file=f)
os.remove("outText.txt")
