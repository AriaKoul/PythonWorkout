import random

def guessing_game():
    number = random.randint(0, 100)
    while True:
        guess = int(input('Enter your guess here: '))
        if guess > number:
            print('Too high! Guess again!')
        elif guess < number:
            print('Too low! Guess again!')
        elif guess == number:
            print(f'You got it! The answer is {guess}')
            break


guessing_game()