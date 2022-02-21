def get_sv(filename):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    f = open(filename)
    return {word.strip()
            for word in f 
            if vowels < set(word.lower())}

