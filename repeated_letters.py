import operator
from collections import Counter


WORDS = ['this', 'is', 'an', 'elementary', 'test', 'example']

def most_repeating_letter_count(word):
    return Counter(word).most_common(1)[0][1]


def most_repeating_word(sequence):
    return max(sequence, key = most_repeating_letter_count(1)[0][1])


print(most_repeating_word(WORDS))
