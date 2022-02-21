from fileinput import filename
import os

def find_longest_word(filename):
    longest_word = ''
    f = open(filename)
    for line in f:
        for word in line.split():
            if len(word) > len(longest_word):
                longest_word = word 
    return longest_word


def find_all_longest_words(directory):
    return {filename: find_longest_word(os.path.join(directory, filename))
    for filename in os.listdir(directory)
    if os.path.isfile(os.path.join(directory, filename))}

print(find_all_longest_words('.'))