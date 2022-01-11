import random

print('Welcome to Hangman!')

words = ['python', 'java', 'kotlin', 'javascript']  # list of words
word = random.choice(words)  # random word from list

guesses = ''  # empty string
turns = 10  # number of turns

while turns > 0:
    failed = 0  # number of failed attempts
    for char in word:  # for each character in word
        if char in guesses:  # if character is in guesses
            print(char, end='')  # print character from word in guesses string 
        else:  # if character is not in guesses
            print('_', end='')  # print underscore instead
            failed += 1  # add 1 to failed attempts

    if failed == 0: # if failed attempts is 0
        print('\nYou won!') # print you won
        break # break the loop

    print() # print new line

    guess = input('Guess a character: ') # input guess
    guesses += guess # add guess to guesses string

    if guess not in word: # if guess is not in word
        turns -= 1 # subtract 1 from turns
        print('No such character in the word.') # print no such character in the word
        print('You have', turns, 'more guesses.') # print you have turns more guesses
        if turns == 0: # if turns is 0
            print('You lost!') # print you lost
    