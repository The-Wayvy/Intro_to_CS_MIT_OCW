# 6.00 Problem Set 4
#
# Caesar Cipher Skeleton
#
import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
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
    line = inFile.readline() #turns entire file into a string?
    # wordlist: list of strings
    wordlist = line.split()
    print "  ", len(wordlist), "words loaded."
    return wordlist

wordlist = load_words()

def is_word(wordlist, word):
    """
    Determines if word is a valid word.

    wordlist: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordlist.

    Example:
    >>> is_word(wordlist, 'bat') returns
    True
    >>> is_word(wordlist, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in wordlist

def random_word(wordlist):
    """
    Returns a random word.

    wordlist: list of words
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

def random_string(wordlist, n):
    """
    Returns a string containing n random words from wordlist

    wordlist: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([random_word(wordlist) for _ in range(n)])

def random_scrambled(wordlist, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordlist: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words


    NOTE:
    This function will ONLY work once you have completed your
    implementation of apply_shifts!
    """
    s = random_string(wordlist, n) + " "
    shifts = [(i, random.randint(0, 26)) for i in range(len(s)) if s[i-1] == ' '] # Ha! [-1] is a ' ' so we count the first word.
    return apply_shifts(s, shifts)[:-1]

def get_fable_string():
    """
    Returns a fable in encrypted text.
    """
    f = open("fable.txt", "r")
    fable = str(f.read())
    f.close()
    return fable


# (end of helper code)
# -----------------------------------

#
# Problem 1: Encryption
#
def build_coder(shift):

    assert shift > - 27 and shift < 27

    Capitals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                ' ']
    Lowers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              ' ']

    Mapper = {}

    for character in Capitals:
        new_index = Capitals.index(character) + shift
        if new_index > 26:
            new_index -= 27
        elif new_index < -26:
            new_index += 27
        Mapper[character] = Capitals[new_index]

    for character in Lowers:
        new_index = Lowers.index(character) + shift
        if new_index > 26:
            new_index -= 27
        elif new_index < -26:
            new_index += 27
        Mapper[character] = Lowers[new_index]

    return Mapper

    """
    Returns a dict that can apply a Caesar cipher to a letter.
    """
    """
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: -27 < int < 27
    returns: dict

    Example:
    >>> build_coder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (The order of the key-value pairs may be different.)

    Plan:
    ~ check to make sure shift is in range
    ~ create two alphabetical lists, one capital one lowercase
    ~ create a dictionary mapping characters to characters
    ~ For each letter in each list, add shift to its index. Then create a
        dictionary entry where the key is the letter, and the value is the lette
        r at index + shift in the same list. If a new index > 26, subtract 27. I
        f a new index < 0 then add 27. If char not in list map it to itself.
    ~ return the dictionary
    """


def build_encoder(shift):
    """
    Returns a dict that can be used to encode a plain text.
    """

    encoder = build_coder(shift)
    return encoder
    # Note that although build_coder returns something, build_encoder doesn't
    # until you actually have a return statement on the page

    """
    For example, you could encrypt the plain text by calling the following commands
    >>>encoder = build_encoder(shift)
    >>>encrypted_text = apply_coder(plain_text, encoder)

    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: 0 <= int < 27
    returns: dict

    Example:
    >>> build_encoder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (The order of the key-value pairs may be different.)

    HINT : Use build_coder.
    """

def build_decoder(shift):

    """
    Returns a dict that can be used to decode an encrypted text.
    ???identical with build_encoder, waste of memory???
    """

    decoder = build_coder(shift)
    return decoder

    """
    For example, you could decrypt an encrypted text by calling the following commands
    >>>encoder = build_encoder(shift)
    >>>encrypted_text = apply_coder(plain_text, encoder)
    >>>decrypted_text = apply_coder(plain_text, decoder)

    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: 0 <= int < 27
    returns: dict

    Example:
    >>> build_decoder(3)
    {' ': 'x', 'A': 'Y', 'C': ' ', 'B': 'Z', 'E': 'B', 'D': 'A', 'G': 'D',
    'F': 'C', 'I': 'F', 'H': 'E', 'K': 'H', 'J': 'G', 'M': 'J', 'L': 'I',
    'O': 'L', 'N': 'K', 'Q': 'N', 'P': 'M', 'S': 'P', 'R': 'O', 'U': 'R',
    'T': 'Q', 'W': 'T', 'V': 'S', 'Y': 'V', 'X': 'U', 'Z': 'W', 'a': 'y',
    'c': ' ', 'b': 'z', 'e': 'b', 'd': 'a', 'g': 'd', 'f': 'c', 'i': 'f',
    'h': 'e', 'k': 'h', 'j': 'g', 'm': 'j', 'l': 'i', 'o': 'l', 'n': 'k',
    'q': 'n', 'p': 'm', 's': 'p', 'r': 'o', 'u': 'r', 't': 'q', 'w': 't',
    'v': 's', 'y': 'v', 'x': 'u', 'z': 'w'}
    (The order of the key-value pairs may be different.)

    HINT : Use build_coder.
    """

def apply_coder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.
    """

    coded_string = ''

    for character in text:
        if character in coder:
            coded_string += coder[character]
        else:
            coded_string += character

    return coded_string


    """
    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text

    Example:
    >>> apply_coder("Hello, world!", build_encoder(3))
    'Khoor,czruog!'
    >>> apply_coder("Khoor,czruog!", build_decoder(3))
    'Hello, world!'

    Plan:
    ~ Create an empty string
    ~ For each character in text, if character not in text then add it to the
    new string, else use the coder to add its mapping to the string.
    ~ Return the string
    """

def apply_shift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift offset.
    ???Why do we need this. Answer: it builds a coder for you???
    """

    Cipher = build_encoder(shift)

    Cipher[' '] = Cipher[' '].lower()

    Caesar_Ciphered = apply_coder(text, Cipher)

    return Caesar_Ciphered

    """
    The empty space counts as the 27th letter of the alphabet,
    so spaces should be replaced by a lowercase letter as appropriate.
    Otherwise, lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text
    returns: text after being shifted by specified amount.

    Example:
    >>> apply_shift('This is a test.', 8)
    'Apq hq hiham a.'
    """

#
# Problem 2: Codebreaking.
#
def find_best_shift(wordlist, text):
    """
    Return the shift which produces only correct words and at least as many words as any shift which produces only correct words.
    """

    best_shift = 0
    max_words = 0

    for shift in range(-26, 27):
        decyphered = apply_shift(text, shift)
        decyphered_words = string.split(decyphered)
        num_words = 0
        for word in decyphered_words:
            if not is_word(wordlist, word):
                num_words = 0
                break
            else: num_words += 1
        if num_words > max_words:
            max_words = num_words
            best_shift = shift

    return best_shift
    """
    text: string
    returns: 0 <= int 27

    Example:
    >>> s = apply_coder('Hello, world!', build_encoder(8))
    >>> s
    'Pmttw,hdwztl!'
    >>> find_best_shift(wordlist, s) returns
    8
    >>> apply_coder(s, build_decoder(8)) returns
    'Hello, world!'
    Plan:
    ~ Loop through -26 and 26.
    ~ Apply decoder for each value. Store the result
    ~ Count the number of spaces, add 1, this gives the number of words.
    ~ Break the string into a list of strings representing words. Check validity
    ~ Ignore any shifts with invalid words.
    ~ Create a dictionary where keys are the shift and values the # of words
    ~ Find the key which returns the greatest number of words and return that key
    """

#
# Problem 3: Multi-level encryption.
#
def apply_shifts(text, shifts):
    """
    Applies a sequence of shifts to an input text and returns a string.
    """
    entire_text = text[:]

    for shft in shifts:
        unmodified_text = entire_text[:shft[0]]
        modified_text = apply_shift(entire_text[shft[0]:], shft[1])
        entire_text = unmodified_text + modified_text

    return entire_text

    """
    text: A string to apply the Ceasar shifts to
    shifts: A list of tuples containing the location each shift should
    begin and the shift offset. Each tuple is of the form (location,
    shift) The shifts are layered: each one is applied from its
    starting position all the way through the end of the string.
    returns: text after applying the shifts to the appropriate
    positions

    Example:
    >>> apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    """

#
# Problem 4: Multi-level decryption.
#


def find_best_shifts(wordlist, text, start=0):
    """
    Given a scrambled string, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.
    """

    all_shifts = []

    if len(text) == len(text[0:start-1]):
        return []
               
    else:
        for shift in range(-26, 27):
      #      print shift
            partial_decyph = apply_shift(text[start:],shift)
            partial_list = string.split(partial_decyph)
            if is_word(wordlist, partial_list[0]):
                text = text[0:start] + partial_decyph
    #            print text
                all_shifts = all_shifts + [(start,shift)] + find_best_shifts(wordlist, text, (len(text) - len(partial_decyph) + len(partial_list[0]) + 1))
     #           print "uh oh!"
                break
        
    return all_shifts

print find_best_shifts(wordlist, 'dbualvclgzfvjlqrwni ookd')
"""
    Hint: Make use of the recursive function
    find_best_shifts_rec(wordlist, text, start)

    wordlist: list of words
    text: scambled text to try to find the words for
    returns: list of tuples.  each tuple is (position in text, amount of shift)

    Examples:
    >>> s = random_scrambled(wordlist, 3)
    >>> s
    'eqorqukvqtbmultiform wyy ion'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> shifts
    [(0, 25), (11, 2), (21, 5)]
    >>> apply_shifts(s, shifts)
    'compositor multiform accents'
    >>> s = apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    >>> s
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> print apply_shifts(s, shifts)
    Do Androids Dream of Electric Sheep?
    """

def decrypt_fable():
    """Prints the decrypted fable"""

    the_fable = get_fable_string()    
    the_shift = find_best_shifts(wordlist,the_fable)
    print the_shift
    the_message = apply_shifts(the_fable,the_shift)
    print the_message

    """
    Using the methods you created in this problem set,
    decrypt the fable given by the function get_fable_string().
    Once you decrypt the message, be sure to include as a comment
    at the end of this problem set how the fable relates to your
    education at MIT.

    returns: string - fable in plain text
    """

decrypt_fable()

#What is the moral of the story?
# Everyone makes mistakes               
#
#
#
#

