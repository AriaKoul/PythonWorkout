def join_numbers(range_of_integers):
    return ', '.join(str(number) for number in range_of_integers)


print(join_numbers(range(15)))