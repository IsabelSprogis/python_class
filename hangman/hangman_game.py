# Writer: Isabel Cristina Sarti Sprogis
# Python and O.O online course from Caelum
# 16/03/2021 from 8:00 to 12:00
import random
import hangman.funcoes_forca as draw


def print_banner():
    print('* * * * * * * * * * * * * * * * * * * * * * *')
    print('*       Welcome to the Hangman Game!        *')
    print('* * * * * * * * * * * * * * * * * * * * * * *')


def game_win(secret_word):
    draw.imprime_mensagem_vencedor()
    print('* * * * * * You have won! * * * * * *')
    print(f'The word was: {secret_word} \n')


def game_lose(secret_word):
    draw.imprime_mensagem_perdedor(secret_word)
    print("* * * * * * You have Lost! * * * * * *")
    print(f'The word was: {secret_word} \n')


def create_words_database():
    # Writing words for our words database in a txt file
    # words = ("python", "banana", "google", "answer", "padtec", "wss", "tester", "server", "object", "game", "day", "life")
    word = open('hangman_words.txt', 'w')
    word.write('python\n')
    word.write('banana\n')
    word.write('google\n')
    word.write('answer\n')
    word.write('padtec\n')
    word.write('wss\n')
    word.write('tester\n')
    word.write('server\n')
    word.write('object\n')
    word.write('game\n')
    word.write('day\n')
    word.write('life\n')
    word.flush()
    word.close()

    # appending a new word on the words txt file
    word = open('hangman_words.txt', 'a')
    word.write('laranja\n')
    word.flush()
    word.close()


def return_secret_word():
    # opening the word txt file in read mode to selecet a random word
    word = open('hangman_words.txt').read().splitlines()
    chosen_word = random.choice(word)
    return chosen_word


def create_mock_word(secret_word):
    mock_word = list(secret_word)
    for i in range(len(secret_word)):
        mock_word[i] = ' _ '

    return mock_word


def guess(secret_word, mock_word):
    win = False
    lose = False
    error_count = 0
    correct_count = 0

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
            draw.desenha_forca(error_count)
            print(f'Error count: {error_count}')

        win = correct_count == len(secret_word)
        lose = error_count == len(secret_word)

    return win, lose


def hangman():
    create_words_database()
    secret_word = return_secret_word()
    mock_word = create_mock_word(secret_word)
    print_banner()
    win_game, lose_game = guess(secret_word, mock_word)

    if win_game:
        game_win(secret_word)
    else:
        game_lose(secret_word)


if __name__ == '__main__':
    hangman()
