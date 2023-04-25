import random

from art import logo
print(logo)

print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 10
if difficulty == 'hard':
    attempts = 5

numberGuessed = False

while not numberGuessed and attempts != 0:
    guess = int(input('Make a guess: '))
    if guess > number:
        attempts -= 1
        print('Too high')
        print('Guess again.')
        print(f'You have {attempts} attempts remaining to guess the number.')
    elif guess < number:
        attempts -= 1
        print('Too low')
        print('Guess again.')
        print(f'You have {attempts} attempts remaining to guess the number.')
    elif guess == number:
        print(f'You got it! the answer was {number}')
        numberGuessed = True

if attempts == 0:
    print('You ran out of attempts. You lose')
