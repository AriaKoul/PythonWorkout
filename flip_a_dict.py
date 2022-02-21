
def flip_a_dict(dict):
    return {value: key for key,value in dict.items()}

print(flip_a_dict({'a':1, 'b':2, 'c':3}))