# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
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

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

def game(word):
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(word)) + " letters long."
    used = []
    guesses = len(word) * 2
    while guesses > 0:
        progress = ""
        print "You have " + str(guesses) + " guesses left."
        guess = raw_input("Guess a letter. ")
        if guess in word:
            "Score! " + guess + " is in the word."
            used.append(guess)
            for letter in word:
                if letter in used:
                    progress = progress + letter
                else:
                    progress = progress + "_"
            if "_" not in progress:
                print "You won!"
                print "Here's your word: " + progress
                break
            else:
                print progress
                print used
        else:
            used.append(guess)
            print "sorry, " + guess + " isn't in my word."
            print "you've used: ", used
            guesses -= 1
    else:
        print "you lose, my word was: " + word

game(choose_word(wordlist)) 
