from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    best_word = None
    best_score = 0
    for word_size in range(1,HAND_SIZE+1):
        words = get_perms(hand,word_size)
        for word in words:
            if is_valid_word(word,hand,word_list) and get_word_score(word,HAND_SIZE) > best_score:
                best_score = get_word_score(word,HAND_SIZE)
                best_word = word
    return best_word
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
    total_score = 0
    while True:
        print "AI's remaining letters"
        display_hand(hand)
        comp_choice = comp_choose_word(hand,word_list)
        if comp_choice == None:
            break
        else:
            comp_score = get_word_score(comp_choice,HAND_SIZE)
            total_score += comp_score
            hand = update_hand(hand,comp_choice)
            print "AI chose",comp_choice,",which scored",comp_score
    print "AI's hand score:",total_score
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
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

    def pick_player():
        player = raw_input("who will play? u: you, or c: computer? ")
        while player != "u" and player != "c":
            print "that's not an option"
            player = raw_input("who will play? u: you, or c: computer? ")
        return player

    def pick_next_game():
        game = raw_input("n: new hand, r: same hand, e: exit: ")
        while game != 'e' and game != 'r' and game != 'n':
            print "that's not an option!"
            game = raw_input("n: new hand, r: same hand, e: exit: ")
        return game

    old_hand = deal_hand(HAND_SIZE) 
    player = pick_player()
    if player == 'u':
        play_hand(old_hand,word_list)
    else:
        comp_play_hand(old_hand,word_list)
    while True:
        option = pick_next_game()
        if option == "e":
            print "goodbye!"
            break   
        elif option == "r":
            option = pick_player()
            print "============================="
            if option == 'u':
                play_hand(old_hand,word_list)
            else:
                comp_play_hand(old_hand,word_list)
        else:
            old_hand = deal_hand(HAND_SIZE)
            option = pick_player()
            print "=============================="
            if option == "u":
                play_hand(old_hand,word_list)
            else:
                comp_play_hand(old_hand,word_list)
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

    
