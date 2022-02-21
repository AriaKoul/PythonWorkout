import random

def create_password_generator(characters):
    def create_password(length):
        output = []
        for j in range(length):
            output.append(random.choice(characters))
        return ''.join(output)
    return create_password

alphabet_password = create_password_generator('abcdef')
symbol_password = create_password_generator('!@#$%')

print(alphabet_password(5))
print(alphabet_password(10))

print(symbol_password(5))
print(symbol_password(10))
