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
    line = inFile.readline()
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
    shifts = [(i, random.randint(0, 26)) for i in range(len(s)) if s[i-1] == ' ']
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
    """
    Returns a dict that can apply a Caesar cipher to a letter.
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
    """
    ups = string.ascii_uppercase + " "
    downs = string.ascii_lowercase + " "
    coder = {}

    if shift < 0:
    	shift += 27

    for alphabet_index in range(27):
    	code_index = (alphabet_index+shift)%27
    	coder[ups[alphabet_index]] = ups[code_index]
    	coder[downs[alphabet_index]] = downs[code_index]

    return coder


def build_encoder(shift):
    """
    Returns a dict that can be used to encode a plain text. For example, you
    could encrypt the plain text by calling the following commands
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
    """

    return build_coder(shift)


def build_decoder(shift):
    """
    Returns a dict that can be used to decode an encrypted text. For example, you
    could decrypt an encrypted text by calling the following commands
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
    """

    return build_coder(-shift)

def apply_coder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text

    Example:
    >>> apply_coder("Hello, world!", build_encoder(3))
    'Khoor,czruog!'
    >>> apply_coder("Khoor,czruog!", build_decoder(3))
    'Hello, world!'
    """
    encoded_text = ""
    for character in text:
    	if character.isalpha() or character == " ":
    		encoded_text += coder[character]
    	else:
    		encoded_text += character
    return encoded_text  

def apply_shift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. The empty space counts as the 27th letter of the alphabet,
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
    return apply_coder(text,build_encoder(shift))
   
#
# Problem 2: Codebreaking.
#

def count_words(wordlist,text):
	"""
	takes a text and counts the number of words in it

	wordlist : list
	text: string

	returns : int
	"""
	split_text = text.split(" ")
	word_count = 0
	for word in split_text:
		if is_word(wordlist,word):
			word_count += 1
		else:
			break
	return word_count

def tie_break(wordlist,text,shift1,shift2):
	'''
	takes two shifts which produce the same number of valid words 
	and returns the one that produces longer words

	text: string
	shift1: int
	shift2: int

	returns: int
	'''
	shifted_text1 = apply_coder(text,build_decoder(shift1))
	shifted_text2 = apply_coder(text,build_decoder(shift2))
	split_text1 = shifted_text1.split(" ")
	split_text2 = shifted_text2.split(" ")
	length_1 = 0
	length_2 = 0
	for word in split_text1:
		if is_word(wordlist,word):
			length_1 += len(word)
		else:
			break
	for word in split_text2:
		if is_word(wordlist,word):
			length_2 += len(word)
		else:
			break	  
	if length_1 > length_2:
		return shift1
	else:
		return shift2


def find_best_shift(wordlist, text):
	"""
	Decrypts the encoded text and returns the plaintext.

	text: string
	returns: 0 <= int < 27

	Example:
	>>> s = apply_coder('Hello, world!', build_encoder(8))
	>>> s
	'Pmttw,hdwztl!'
	>>> find_best_shift(wordlist, s) returns
	8
	>>> apply_coder(s, build_decoder(8)) returns
	'Hello, world!'
	"""
	best_shift = None
	num_words_in_best_shift = 0

	for shift in range(27):
		shifted_text = apply_coder(text,build_decoder(shift))
		word_count = count_words(wordlist,shifted_text)
		if word_count > num_words_in_best_shift:
			num_words_in_best_shift = word_count
			best_shift = shift
		elif word_count == num_words_in_best_shift and word_count != 0:
			best_shift = tie_break(wordlist,text,best_shift,shift)
	return best_shift

#
# Problem 3: Multi-level encryption.
#
def apply_shifts(text, shifts):
	"""
	Applies a sequence of shifts to an input text.

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

	for location,shift in shifts:
		text = text[:location] + apply_coder(text[location:],build_encoder(shift))

	return text 

def reverse_shifts(text,shifts):
	"""
	decode a string that has been encrypted with shifts

	text: string
	shifts: list of tuples

	return: string
	"""
	for location,shift in shifts:
		text = text[:location] + apply_coder(text[location:],build_decoder(shift))

	return text 

 
#
# Problem 4: Multi-level decryption.
#


def find_best_shifts(wordlist, text):
	"""
	Given a scrambled string, returns a shift key that will decode the text to
	words in wordlist, or None if there is no such key.

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
	start = 0
	shifts = []
	while start < len(text):
		print text
		next_shift = find_best_shift(wordlist,text[start:])
		shifts.append((start,next_shift))
		text = text[:start] + apply_coder(text[start:],build_decoder(next_shift))	
		start = new_start(wordlist,text) 
	return shifts


def new_start(wordlist,text):
	"""
	Given a partially decoded string, returns the index from which
	to start the next round of decoding

	text: string
	returns: int
	"""
	start_index = 0
	words = text.split(" ")
	for word in words:
		if is_word(wordlist,word):
			start_index += (len(word)+1)
		else:
			break
	return start_index

def decrypt_fable():
	"""
	Using the methods you created in this problem set,
	decrypt the fable given by the function get_fable_string().
	Once you decrypt the message, be sure to include as a comment
	at the end of this problem set how the fable relates to your
	education at MIT.

	returns: string - fable in plain text
	"""
	fable = get_fable_string()
	best_shifts = find_best_shifts(wordlist,fable)
	print reverse_shifts(fable,best_shifts)



#What is the moral of the story?
#
#
#
#
#

