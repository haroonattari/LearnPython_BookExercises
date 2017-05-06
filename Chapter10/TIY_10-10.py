import re
from collections import defaultdict

filename = 'gutenberg.txt'

wordlist = defaultdict(int)

try:

    with open(filename) as file_object:
        lines = file_object.readlines()
        for line in lines:
            words = line.strip().split(' ')
            for word in words:
                wordlist[word.lower()] = wordlist[word.lower()] + 1

    for word,count in wordlist.items():
        print(word, count)

except FileNotFoundError as filenotfoundex:
    print("Error opening file")

