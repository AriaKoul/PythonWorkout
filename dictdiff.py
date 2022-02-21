def dictdiff(first_dict, second_dict):
    output = {}
    all_keys = first_dict.keys() | second_dict.keys()
    for key in all_keys:
        if first_dict.get(key) != second_dict.get(key):
            output[key] = [first_dict.get(key), second_dict.get(key)]

    return output 

d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'd':4}

print(dictdiff(d1, d2))
