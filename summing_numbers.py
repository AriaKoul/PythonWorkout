
def my_sum(*numbers):
    output = 0
    for number in numbers:
        output+= number
    return output

print(my_sum(2, 5, 17, 87))