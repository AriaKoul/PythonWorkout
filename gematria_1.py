import string

def gematria_dict():
    {char: index 
        for index, char 
            in enumerate(string.ascii_lowercase, 1)}

GEMATRIA = gematria_dict()

def gematria_for(word):
    return sum(GEMATRIA.get(one_char,0)
                for one_char in word)

def gematria_equal_words(input_word):
    our_score = gematria_for(input_word.lower())
    return [one_word.strip() 
            for one_word in open('/usr/share/dict/words')
            if gematria_for(one_word.lower()) == our_score]

print(gematria_for("cat"))

