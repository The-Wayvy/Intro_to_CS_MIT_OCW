# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def print_word(word,guessed_letters):
    to_print = ""
    for letter in word:
        if letter in guessed_letters:
            to_print += letter
        else:
            to_print += "?"
    return to_print

def finished(word,guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    else:
        return True

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

secret_word = choose_word(wordlist)
guesses_remaining = 7
guessed_letters = []

print "Welcome to hangman!"
while guesses_remaining > 0:
    print "=========================================="
    print "you have",guesses_remaining,"guesses left"
    print "you've guessed the following letters",guessed_letters
    print "the word so far:",print_word(secret_word,guessed_letters)
    guess = raw_input("guess a letter: ")
    while guess in guessed_letters:
        print "you already guessed that!"
        guess = raw_input("guess a letter: ")
    if guess in secret_word:
        print "good guess"
        guessed_letters.append(guess)
        if finished(secret_word,guessed_letters):
            print "=================================="
            print "You win!"
            print "the word was",secret_word,"!!"
            break
    else:
        print "sorry"
        guesses_remaining -= 1
        guessed_letters.append(guess)
else:
    print "==============================="
    print "sorry, you lost"
    print "the word was",secret_word