"""
MIT intro to CS with Python
Problem Set 0
"""
"""
x = raw_input("What is your date of birth?")
y = raw_input("What is your last name?")

print y, x
"""

"""
NOTES
"""

"""
input('string')
prints the string, then takes user input, then evaluates the input as python code and finally returns the result

a = input('how old are you?')
print a

# Entering sum([1, 2, 3, 4, 5, 6]) will return 21.

Appparently this is the RECOMENDED substitute for input()

x = None
while not x:
    try:
        x = int(raw_input())
    except ValueError:
        print 'Invalid Number'

for i in range (1, 11):
    print i,
for i in range (11, 21):
    print i,
# This will print all the numbers on one line. To seperate them:

for i in range (1, 11):
    print i,
print
for i in range (11, 21):
    print i,

x = 7
print (x)

# Backslash is used to 'escape' a single or double quote, ie. to print it as a string rather than interpret it as an operation. Likewise the backslash needs to be escaped.
# Ex. print "\" returns an error, while print "\\" returns a string: \

food = raw_input()
print "you had " + food + "! That sounds delicious."
apple = food + 5 # This returns an error because food is a string, even if you enter an integer.
# Raw input converts all input into a string.

print "blah",
exc = raw_input()
#This code is all printed on one line.

print "I am {0}".format(42)
will return 'I am 42'

x = input("lala")
y = x + 2
print y
# This works because input interprets an integer as an integer. No conversion into strings.

a_string = raw_input("Enter a string, comrade.")
print len(a_string)

word = raw_input("Type a word, comrade.")
times = input("Type an integer, comrade.")
print word * times
"""
