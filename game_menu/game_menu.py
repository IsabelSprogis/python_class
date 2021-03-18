# Writer: Isabel Cristina Sarti Sprogis
# Python and O.O online course from Caelum
# 18/03/2021 from 8:00 to 12:00
import hangman.hangman_game as hg
# from hangman.hangman_game import hangman
# import guess_number.guess_number_game
from guess_number.guess_number_game import guess_number

exit_state = False

print('* * * * * * * * * * * * * * * * * * * * * * *')
print('*      WELCOME TO THE GAME STATION          *')
print('* * * * * * * * * * * * * * * * * * * * * * *')

while exit:
    mode = input('Choose which game to play: \n 1) Hangman \n 2) Guess the Number \n exit- to exit the game \n')
    if mode == "1":
        # hangman.hangman_game.hangman()
        hg.hangman()
    elif mode == "2":
        guess_number.guess_number_game.guess_number()
    elif mode == 'exit':
        exit_state = True

