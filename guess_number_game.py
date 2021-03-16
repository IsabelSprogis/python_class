# Writer: Isabel Cristina Sarti Sprogis
# Python and O.O online course from Caelum
# 15/03/2021 from 8:00 to 12:00
from random import randrange
secret_number = randrange(20)
count = 0
difficulty_setting = None
max_tries = 0

print('* * * * * * * * * * * * * * * * * * * * * * *')
print('*     Guess the Secret Number Game!         *')
print('* * * * * * * * * * * * * * * * * * * * * * *')

difficulty_setting = input('Enter a difficulty setting: EASY | MEDIUM | HARD: \n')
if difficulty_setting.upper() == 'EASY':
    max_tries = 10
    print(f'Max tries: {max_tries}')
elif difficulty_setting.upper() == 'MEDIUM':
    max_tries = 5
    print(f'Max tries: {max_tries}')
elif difficulty_setting.upper() == 'HARD':
    max_tries = 3
    print(f'Max tries: {max_tries}')
else:
    print('please provide a real difficulty setting!')

while count < max_tries:
    print('* * * * * * * * * * * * * * * * * * * * * * *')
    print('*     Guess the Secret Number Game!         *')
    print('* * * * * * * * * * * * * * * * * * * * * * *')

    user_guess = int(input('Guess the sorted secret number:'))

    correct_answer = user_guess == secret_number
    higher = user_guess > secret_number
    lower = user_guess < secret_number

    if correct_answer:
        print(f'You Won! The secret number was: {secret_number}')
        print(f'Necessary tries:{count + 1}')
        break
    elif higher:
        print('The Guess is Higher than the secret number')
        print(f'Current try:{count + 1}')
    elif lower:
        print('The Guess is lower than the secret number')
        print(f'Current try:{count + 1}')

    count += 1
print('Max tries reached')
print(' * * * * * END GAME * * * * *')
