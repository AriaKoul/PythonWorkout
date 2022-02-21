from freedonia import calculate_tax

tax_at_noon = calculate_tax(100, 'Harpo', 12)
tax_at_9pm = calculate_tax(100, 'Harpo', 21)

print(f"Your total cost is {tax_at_noon} if purchasing at 12pm.")
print(f"Your total cost is {tax_at_9pm} if purchasing at 9pm.")