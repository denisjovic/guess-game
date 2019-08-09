import random

name = input('Hi, what is your name? \n')
print('Hi {}. Can you guess my number, its between 1 and 20?'.format(name))
secret_number = random.randint(1,20)

for guesses in range(1,7):
    guess = int(input())
    if guess > secret_number:
        print('That is too high')
    elif guess < secret_number:
        print('That is too low')
    else:
        break

if guess == secret_number:
    print('Well done, you needed {} times to get the secret number!'.format(guesses))
else:
    print('Sorry, correct answer was {}'.format(secret_number))
