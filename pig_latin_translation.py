def plword(word):
    if word[0] in "aeiou":
        return f"{word}way"
    else:
        return f"{word[1:]}{word[0]}ay"

def plfile(filename):
    f = open(filename)
    return ' '.join(plword(one_word)
    for one_line in f
    for one_word in one_line.split())
