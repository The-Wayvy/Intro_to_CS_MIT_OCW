from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#
def letters_left(hand):
    Total = 0
    for letter in hand:
        Total += hand[letter]
    return Total


def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    q = letters_left(hand)
    final_max = ''
    valid_words = []
    for n in range(1, q + 1):
        for word in get_perms(hand, n):
            if is_valid_word(word, hand, word_list):
                valid_words.append(word)
    if valid_words == []:
        return None
    final_max = reduce(lambda x, y: x if get_word_score(x, q) >= get_word_score(y,q) else y, valid_words)
    return final_max


def play_again(word_list, original_hand):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """

    play_quit = raw_input('play again? ')
    if play_quit == 'n':
        who = raw_input('you or compuer? ')
        while who != 'c' and who != 'u':
            who = raw_input('you or compuer? ')
        if who == 'c':
            comp_play_hand(deal_hand(random.randrange(1, 9)),word_list)
        else:
            play_hand(deal_hand(random.randrange(1, 9)),word_list)
    elif play_quit == 'r':
        who = raw_input('you or compuer? ')
        while who != 'c' and who != 'u':
            who = raw_input('you or compuer? ')
        if who == 'c':
            comp_play_hand(original_hand, word_list)
        else:
            play_hand(original_hand, word_list)
    elif play_quit == 'e':
        print "thanks for playing"
    else:
        print "incorrect input"
        play_again(word_list, original_hand)

               

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    original_hand = hand.copy()
    Score = 0
    total_letters = letters_left(hand)
    display_hand(hand)    
    while comp_choose_word(hand, word_list) != None:
        a_word = comp_choose_word(hand, word_list)
        print "computer guessed " + a_word
        Score += get_word_score(a_word, total_letters)
        print "current score: " + str(Score)
        hand = update_hand(hand, a_word)
    else:
        print 'computer\'s final score is ' + str(Score)

    play_again(word_list, original_hand)

comp_play_hand(deal_hand(random.randrange(1, 9)),word_list)
    
#
# Problem #6C: Playing a game
#
#

#
# Build data structures used for entire session and play game
#
"""
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

    """
