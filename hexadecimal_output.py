
def hex_output():
    decimal_number = 0
    hexadecimal_number = input("Enter a hexadecimal number to convert here: ")

    for power, digit in enumerate(reversed(hexadecimal_number)):
        decimal_number += int(digit, 16) * (16**power)
    print(decimal_number)

hex_output()