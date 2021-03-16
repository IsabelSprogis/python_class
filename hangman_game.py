# Writer: Isabel Cristina Sarti Sprogis
# Python and O.O online course from Caelum
# 16/03/2021 from 8:00 to 12:00
import random

words = ("python", "banana", "google", "answer", "padtec", "wss", "tester", "server", "object", "game", "day", "life")
secret_word = random.choice(words)
win = False
lose = False
error_count = 0
correct_count = 0
mock_word = list(secret_word)
for i in range(len(secret_word)):
    mock_word[i] = ' _ '

print('* * * * * * * * * * * * * * * * * * * * * * *')
print('*       Welcome to the Hangman Game!        *')
print('* * * * * * * * * * * * * * * * * * * * * * *')
while not win and not lose:
    print(mock_word)
    user_guess = input('Enter a letter:')
    user_guess = user_guess.lower()

    if user_guess in secret_word:
        position = 0
        for letter in secret_word:
            if user_guess == letter:
                mock_word[position] = letter
                print(f'Letter {letter} found at position {position}')
                correct_count += 1
            position += 1
    else:
        error_count += 1
        print(f'Error count: {error_count}')

    win = correct_count == len(secret_word)
    lose = error_count == len(secret_word)

if win:
    print('* * * * * * You have won! * * * * * *')
    print(f'The word was: {secret_word}')
else:
    print("* * * * * * You have Lost! * * * * * *")
    print(f'The word was: {secret_word}')
