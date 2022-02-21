def firstlast(sequence):
    return sequence[:1] + sequence[-1:]
    
    """
    if type(sequence) == str:
        return f"{sequence[0]}{sequence[-1]}"
    elif type(sequence) == list:
        output = []
        output.append(sequence[0])
        output.append(sequence[-1])
        return output
    """

print(firstlast([1, 2, 3, 4]))