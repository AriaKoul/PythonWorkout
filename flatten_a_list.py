def flatten(lst):
    return [element for sublist in lst
    for element in sublist]

print(flatten([[1,2], [3,4], [5,6]]))