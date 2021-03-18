import random
words = []
file = open("C:\\Users\\isprogis\\PycharmProjects\\teste\\hangman_words.txt", 'r')

for line in file:
    words.append(line.strip())
print(words)
index = random.randrange(0, len(words))
print(f'Word at index {index+1}:', words[index])

# Change letters in the word for another symbol

mock_word = [' _ ' for letra in words]
print(mock_word)

