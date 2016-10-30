def letter_counter(one_word):
	count = 0
	for letter in one_word:
		count += 1
	return count
		


def manip(sentence):
	master_list = []
	broken_up = sentence.split()
	for word in broken_up:
		word_desc = []
		word_desc.append(word.upper())
		word_desc.append(word.lower())
		word_desc.append(letter_counter(word))
		master_list.append(word_desc)
	print master_list
	

"""
CHECK
"""


"""
Note: split() returns a list, quite unlike append, which returns None.
""" 	