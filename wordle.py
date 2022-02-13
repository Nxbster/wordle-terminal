from yellow_case import yellow_case
from words import get_all_5_letter_words
import random

target_word = ""
output = ''
guess_count = 0

word_options = get_all_5_letter_words()
target_word = random.choice(word_options)

while guess_count <= 6:
    guess = input(f'Input 5 letter word to guess (Cheat -> "{target_word}"): ')
    if(len(guess) != 5):
        print('Enter a 5 letter word')
        continue

    if(guess != target_word and len(guess) == 5):
        #Check if input is valid 5-letter word
        if(guess not in word_options):
            print('Enter a valid word')
            continue

        yellow_case(target_word, guess)
        guess_count = guess_count + 1

    else:
        yellow_case(target_word, guess)
        print(f'Correct! You guessed the word in {guess_count+1} tries')
        break
