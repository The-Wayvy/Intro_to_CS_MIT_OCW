# 6.00 Problem Set 4
#
# Part 2 - RECURSION
#
# Name          : Solutions
# Collaborators : <your collaborators>
# Time spent    : <total time>

#
# Problem 3: Recursive String Reversal
#
def reverse_string(string):
    def rev_string(string,x=len(string)-1):
        if x == 0:
            return string[0]
        else:
            return string[x] + rev_string(string, x-1)
    answer = rev_string(string)
    return answer

#print reverse_string('abc')
"""
Given a string, recursively returns a reversed copy of the string.
For example, if the string is 'abc', the function returns 'cba'.
The only string operations you are allowed to use are indexing,
slicing, and concatenation.

string: a string
returns: a reversed string
"""
"""

if string == "":
    return ""
else:
    return string[-1] + reverse_string(string[:-1])
"""

#
# Problem 4: Srinian
#
def x_ian(x, word):

    if x[0] not in word:
        return False
    elif len(x) == 1:
        return True
    elif x[0] == word[-1]:
        return False
    else:
        return x_ian(x[1:],word[word.index(x[0])+1:])
            
print x_ian('srini', 'histrionic')
print x_ian('john', 'mahjong')
print x_ian('dina', 'dinosaur')
print x_ian('pangus', 'angus')

    
"""
Given a string x, returns True if all the letters in x are
contained in word in the same order as they appear in x.

>>> x_ian('srini', 'histrionic')
True
>>> x_ian('john', 'mahjong')
False
>>> x_ian('dina', 'dinosaur')
True
>>> x_ian('pangus', 'angus')
False

x: a string
word: a string
returns: True if word is x_ian, False otherwise
"""
"""
if len(x) == 0:
    return True
elif len(word) == 0:
    return False
elif x[0] == word[0]:
    return x_ian(x[1:], word[1:])
else:
    return x_ian(x, word[1:])
"""

#
# Problem 5: Typewriter
#
def insert_newlines(text, line_length):
    if text == "":
        return
    words = text.split()
    counter = 0
    words_length = 0
    while words_length < line_length:
        if counter == len(words):
            break
        if len(words) == 1:
            print words[0]
            break
        else:
            print words[counter],
            words_length = words_length + len(words[counter]) + 1 
            counter += 1
    else:
        print "\n",
        insert_newlines(text[words_length:],line_length)

insert_newlines("hakdf hksd h fks hdfk sd fkjhs dfkhs dkfhsd kfhksdhf kjs dfj dbfkjsd bfskjdf hskdf", 15)


"""
Given text and a desired line length, wrap the text as a typewriter would.
Insert a newline character ("\n") after each word that reaches or exceeds
the desired line length.

text: a string containing the text to wrap.
line_length: the number of characters to include on a line before wrapping
    the next word.
returns: a string, with newline characters inserted appropriately. 
"""
##return insert_newlines_rec(text, line_length, line_length-1)
##
##
##def insert_newlines_rec(text, line_length, rem_length):
##    if text == '':
##        return ''
##    elif text[0] == ' ' and rem_length <= 0:
##        return '\n' + insert_newlines_rec(text[1:], line_length, line_length-1)
##    else:
##        return text[0] + insert_newlines_rec(text[1:], line_length, rem_length-1)
