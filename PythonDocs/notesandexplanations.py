"""
Tutorial Part 3
"""
# Type comments by using a hash! A hash will work until you press enter.
"""
If you want to write a comment formatted with enters
then use triple-quotes
"""
"""
Integer division returns the floor
7 / 3 = 2 and 7 / -3 = -3
"""
"""
= assigns values, == tests for equality
"""
"""
You can assign multiple variables at once: a = b = c = 9 or a, b, c = 1, 2, 3
"""
"""
Python reads code from left to right, top to bottom. Order counts!
"""
"""
Floating Point is a fancy way of saying: a number with a decimal.
Operations which take at least one float as an argument will return a float.
"""
"""
In interactive mode the last printed expression is assigned to the variable _
"""
"""
round(float, int) will return a float rounded to 'int' number of decimals.
Negative ints move to the left of the decimal, positive to the right. A 0 'int'
will round to the nearest one's place.
Ex. round(2.345, 1) == 2.3, round(2.345, 0) == 2, round(2.345, -1) = 0.0
"""
"""
long() does something but I don't know what
"""
"""
complex number are written float + floatj
They can be defined thus: complex(real, imaginary)
Their components can be called by variable_name.real and variable_name.imag
Comps can't be converted to ints and floats by int(complex_number) or float(complex_number) 
but they can be converted by abs(complex_number)		
LEARN: How does one divided two complex numbers?
"""
"""
backslash before, neutralizes apostrophes and quotes in a string.
Ex, print "\"Hooray!\", he yelled." will return "Hooray!, he yelled."
"""
"""
\ at the end of a print line applies the print to the next line,
and prints both lines on the same line.
\n in a print line prints the text following it on a new line.
(how do I get rid of the annoying space this produces on the next line?
\n\ lets you press enter
and apply print to your new line but print it on it's own line
\t inserts an 8 space long tab before the next space.
"""
"""
Triple quotes or apostrophes allow you to move around and start new lines
without using \n, although those commands still work.
"""
"""
r"string" prints all \, \n, and \t's in the string. The string becomes 'raw.'
Although \ gets printed, it retains its function.
New lines and tabs are created without \n and \t. Just use \ and hit enter.
"""
"""
when printing multiple unmodified strings, you can join them with +, they can also
concantenate themselves. However a string and a mod string will not auto-concat.
"""
"""
'string'.strip('chars') will remove any characters in 'chars' from 'string'
and return what remains.
"""
"""
Strings can be repeated with *, ex: print "cat" * 2
"""
"""
You can't reassign characters or substrings in a string
"""
"""
x[:i] + x[i:] == x 
is True
"""
"""
Slices with an above-range end-index or below-range start-index treat end at the last object and start at the first object, respectively.
"""
"""
string[-1] returns the last character in the string.
You can think 
Strings are not rings. Going left, you cannot print the character at the last index directly after the character at the first index;
going right, you cannot print the character at the first index directly after the character at the last index.
"""
"""
A unicode string can be written thus: u'string'
if you have declared a unicode string you can insert raw unicode inside by
typing \u and then entering one 4 digit hexadecimal.
"""
"""
LEARN: You might want to get a handle on Unicode/ASCII/UTF-8/16
"""
"""
numbers and strings are simple data
lists and dictionaries are compound data
lists can be concatenated just like strings, except you need the +.
lists can be repeated just like strings. This will produce one list.
list[:] and string[:] return a copy of the whole.
lists can be modified in many ways. Individual items or slices can be revalued,
items can be inserted, lists can be wiped clean, etc.
You can remove/replace items without using any methods. Like this: list[X:Y] = [] and list[X:Y] = ['whatever', 'and', 'whatever'] 
Note, even if you only want to remove one item, you must have a start and stop index. Using only one index will replace the item with an ACTUAL empty list.
You can insert before the item at index X like this: list[X:X] = ['whatever']
Note, if you want to insert a list then you have to use double brackets, list[Z:Z] = [['shit', 'more_shit']] 
A single list can contain multiple kinds of data, both simple and complex.
You can modify a list within a list.
a = ['cat', 'dog']
b = ['donkey', 'horse', 'cow', a]
c = [b, 'chicken', 'dangerous', 'angst']

c[0][3][1] = 'super-dog'
print c
is totally valid
"""
"""
the body of a loop can be ended with a blank line
"""
"""
Part 4
"""
"""
All functions return 'None'
"""
"""
names = ['albert', 'johnathan', 'kelly']

def remover(a_list):
    for item in a_list:
        if len(item) > 5:
            a_list.remove(item)
    else: return a_list
    
print remover(names)
"""
"""
This returns ['johnathan', 'kelly']
Why? Let's run through it step by step.
1.) the for loop takes argument at a_list[0], that is: 'albert'
2.) len('albert') > 5 so 'albert' is removed from a_list
3.) At the initiation of the for loop, len(a_list) = 3, for has processed one argument. So we go to the next one.
4.) Since we removed 'albert', a_list = ['johnathan', 'kelly']
5.) For loops cycle through arguments by index. The first go took a_list[0], now we take a_list[1]
6.) But since we removed the argument at index 0 in step 2, our second argument is now at index[0], the first index, rather than index[1], the second index.
7.) So for takes 'kelly' and does nothing since 'kelly' has a length of 5.
8.) After 'kelly' the next index position is out of the a_list's range, so we go to the else statement and return our a_list = ['johnathan', 'kelly']


What we can do to avoid this is enter a copy of a_list as the for loop's argument. a_list[:] is a list of all items in a_list but it is not a_list.
So when we delete from a_list we leave the list we've created for our for loop untouched.
"""
"""
a neat little trick: range(len(x))
LEARN: the enumerate() function.
"""
"""
Remember that a break in a for or while loop precludes the execution of the else statement.
"""
"""
a beautiful piece of code in which an outer for loop argument modifies an inner for loop argument.  

for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print n, 'equals', x, '*', n/x
...             break
...     else:
...         # loop fell through without finding a factor
...         print n, 'is a prime number'
"""
"""
LEARN: try loops
We have four kinds of else statements, roughly divided into two types. One which is called in response to the Boolean value, false, and the other in response exhausting all arguments. 
try goes to else when there are no exceptions, for goes to else when it runs through all arguments
if goes to else if the conditional is false, while goes to else when the conditional becomes false.
"""
"""
What is the continue statement good for? Here's some code from the tutorial:

for num in range(2, 10):
    if num % 2 == 0:
        print "found an even number", num
        continue # What the fuck is the point of this? The loop continues on its own.
    else: print 'found a number', num
"""
"""
pass does nothing, it serves as placeholder for all other kinds of text to prevent error.
You can put your interpreter on standby with the code:
while somecondition that's true:
    pass
To break out you hit Ctrl + c
"""
"""
Your first line after defining a function should be something called a docstring, formatted thus:

"""Talks about why this function is important
more detailed description"""

"""
"""
Functions always return None at the end of anything else they return. None will only appear if you print a function that doesn't return any other values.
Function names can be reassigned, and variables can be set equal to an active function: vanity = pythag(100), or vanity = pythag
"""
"""
methods are object type specific functions.
LEARN: global statement
LEARN: raise IOError()
Note: in can be used on strings, if 'string_a' in 'string_b' etc.
"""
"""
Returning any value: number, string, boolean, etc. breaks a while/for loop.
"""
Normally, arguments we declare in a function definition must be supplied at each instance of that function. Ex:
def racer(x):
	print x + 1 
racer(1), racer(2), etc. racer() causes an error: 0 arguments supplied, 1 expected.
However there are several options for declaring optional arguments.

The first method is to declare default values for arguments. If an instance does not supply arguments, the default values will be used instead. Ex:
def racer(x=5):
	print x + 1
We can do racer(3), this prints 4, or we can do racer(), this returns 6.

The second method is to assign a variable to our argument. Ex

y = 4
y = 11 #We might use this if y was dependent on another function whose output varied according to its own input
def racer(x=y):
    y = x + 10
    return y

print y
y = 1
print y
print racer()
print y
print racer(50)
print racer()

>>> 11
1
21
1
60
21

In this case the variable must be valued before the function defintion, as above. It will use the final assignment before its own function definition.
The variable itself can still be changed by direct assignment, y = 4, but not by modfication within the function body.
The argument value can only be reassigned upon instantiation: racer(40) replaces the default value of y for just this one instance; afterwards both the default assignment x
and the variable y retain their original values: 11 and 1, respectively. 
Note: reassigning a variable within a function and returning the variable WILL NOT reassign the variable outside the function, only a direct assignment: y = racer(5) can.
summary, reassigning the argument variable within the function changes neither the variable outside the function nor the default argument.


"""
SIDENOTE

def omfg(x=4):
    print x # 4
    x = x**2
    print x # 16

omfg()


z = 10

def adder(x):
    print z
    y = x + z
    print y

adder(5) # prints 15

def adder(x):
    z = x + z
    print z

adder(5) # returns an error. z is called before being defined. Presumable z = signals a new z variable and wipes out the previous z = 10 assignment.

def adder(x):
    print x + z
    z = x ** 2
    print z

adder(5) # also returns an error. Although the z in x + z occurs before z =, z= retroactively nullifies the assignment z = 10.
# In conclusion: if a variable is initiated outside the scope of a function then any modification of the variable within the function will dissolve the initial valuation.

y = 5
def omg(x=y**2):
    print x # 25
    print y # 5
    print y + y # 10
    print x + y # 30

omg()

y = 5
def omg(x=y):
    y = x + x
    print y

omg() # prints 10
"""
"""
Things work differently with strings. If the default argument is modified within the function, the default value changes. 
A new value inputed in an instance will not change the default. Here is some code from the tutorial:
WTF
def f(a, L=[]):
    L.append(a)
    return L
        
print f(1)
print f(2)
print f(3)
print f(4, ['cats'])
print f(5)

>>> [1]
[1, 2]
[1, 2, 3]
['cats', 4]
[1, 2, 3, 5]


Another option is to set the default value to None. This way internal argument reassignments will not alter the default.

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print f(1)
print f(2)
print f(3)

>>> [1]
[2]
[3]
"""
"""
if multiple defaulted arguments are present, all, some, or none can be instanced in any order by using the argument name. We can also assign values without using the argument
names just as we do for non-defaulted/non-optional arguments. In that case order matters. You can also use a mix of names and no-names. In this case the no-names come first and
the arguments assigned go from left to right

def adder(x=1, y=2, z=3)
	print x + y + z

adder() = 6
adder(3, 4, 5) = 3 + 4 + 5 = 12
adder(z=7, x=5, y=6) = 5 + 6 + 7 = 18
adder(2, z=4, y=8) = 2 + 8 + 4 = 14
"""
Finally, there are arbitrary arguments. There exist two kinds of arbitrary arguments. *name and **name.
*name, creates a tuple(ordered list) based on the values provided at instantiation.
**name, creates a dictionary based on the keys and values provided at instantiation. 
For some reason printing *name, name, **name, and name doesn't work.
Note: order must be observed, first nominal arguments, then tuple arguments, then dictionry arguments.

def some_math(mult, *adds):
    summ = 0
    for num in adds:
        summ += num
    return mult * summ

print some_math(2, 4, 6, 7)


def more_math(div, *adds, **mults):
    summ = sum(adds)
    product = 1
    for num in mults:
        product *= mults[num]
    return (summ + product) / div

print more_math(2, 8, 2, 5, lala=7, po=5)
"""
"""
Unpacking arguments is a neat strategy if you have a multi-argument function and a list/tuple/dictionary containing the desired values.
The order of the dictionary doesn't matter. As if by magic, the keys are matched to the argument variables. I thought keys were strings. 
How is this comparison made?
LEARN: Are argument variables converted into strings when a dictionary is called?
For example:

vals = (12.84, 0)
print round(*vals)

dik = {'B': 'pens', 'A': 'pencils', 'C': 'paper'}

def things_I_have(A="something", B="something", C="something"):
    print "I have " + A + ", " + B + " and " + C + "."

things_I_have()
things_I_have(**dik)  
"""
"""
off-topic: list.sort(function) can use a lambda to sort a list in some special way
LEARN: Lambda wtfwtf
"""
"""
Topic 5
"""
"""
In documentation, square brackets inside parentheses indicate that an argument is optional Ex Function(a, b, [c])
When coding you should say Function(a, b, c=None) and then use an if in the body
"""
"""
If you want to insert at the beggining of a list use list[:0]
LEARN: Why does this work?
If you want to insert at the end of a list use list[len(list):] or list[len(list):0]
This is a little strange because len(list) is out of range.
"""
"""
There are three other common list methods that return something
list.pop([i]) removes and returns the object at index i. If no index is supplied it removes the last object.
list.index(x) returns the first index at which object x occurs.
list.count(x) returns the number of times object x occurs.
Here are five list methods that return None.
list.append(X) adds object X after the last item of list.
list.extend(L) merges L to the end of list.
list.remove(X) removes the first instance of X
list.insert(i,x) inserts object x before the object at index i.
list.reverse() reverses the list
LEARN: list.sort() sorts the list. Takes three other parameters, learn these.
"""
"""
A stack is (a list) like a stack of papers. You can put things on top list.append(x) or take things off the top list.pop()
You can also create a glorified stack called a queue:

from collections import deque
glorified_list = deque(['cat', 'dog', 'frog'])
glorified_list.append('rabbit')
glorfied_list.popleft()
print glorified_list
>>> deque(['dog', 'frog', 'rabbit'])
Apparently this is faster.
"""
"""
A neat peice of code I wrote:

def remover(lister, worder):
    while worder in lister:
        lister.remove(worder)
    else: print lister

remover(['cat', 'cat', 'dog', ['cat', 'notcat', 'cat'], 'dog'], 'cat')
# prints: ['dog', ['cat', 'notcat', 'cat'], 'dog']]

def remover(lister, worder):
    while worder in lister:
        lister.remove(worder)
    for thingy in lister:
        while worder in thingy:
            thingy.remove(worder)
    else: print lister
    
remover(['cat', 'cat', 'dog', ['cat', 'notcat', 'cat'], 'dog'], 'cat')
#prints ['dog', ['notcat'], 'dog']

"""
"""
There is a shorthand version of 

def function(arg):
	if condition:
		print/return arg

It is

def function(arg): print/return condition
"""
"""
filter(boolean_function, object)
takes an object, runs each object in the object through the function and returns only those for which it is true.
This is kind of like a for loop. 

lister = []
for part in object:
	if boolean_function(part) == True:
		lister.append(part)

If you run a dictionary through a filter then you can't look at its values; you can only act on its keys; and it only returns the keys.
LEARN: Is this true? Is filter unable to access a dictionary's values? Is filter useless on dictionaries?

Some examples:
# on a dictionary
def f(x): return x == "A" or x == "D"

dik = {'A': 'cat', 'B': 'frog', 'C': 'ninja', 'D': 'dog'}

print filter(f, dik)
>>> ['A', 'D']

# on a list
def f(x): return x == 'cat'

my_animals = ['cat', 'dog', 'alligator']

print filter(f, my_animals)

>>> ['cat']

# on a string
def f(x): return x == 'c' or x == 't'

cat = 'cat'

print filter(f, cat)

>>> ct	

Using the traditional format

def find(x):
    if 'a' in x:
        return x

print filter(find,['alpha', 'beta', 'psy']) 

>>> ['alpha', 'beta']
"""
"""
map(function, sequence) runs a sequence through a function and then returns the values. Like a for loop.
Ex.
seq = ['tender', 'shiver', 'cadaver']
def adverb(x): return x + 'ly'

print map(adverb, seq)

first = ['sc', 'sa', 'st']
second = ['ab', 'sh', 'op']
def put_together(x, y): return x + y

print map(put_together, first, second)
 
If more than one argument is used then all arguments need to have the same number of objects.
"""
"""
LEARN: string.maketrans()

def are_they_equal(x, y): return x == y

print are_they_equal(1, 1) # prints True

def add_them_up(x, y): return x + y

print add_them_up(1, 1) # prints 2
"""
"""
reduce(function, list, [inital]) returns a single value which is the result of going through list with a binary function, function. If initial is provided then it will be the
first value inputed.

def factorial(x,y): return x * y
n = 5

print reduce(factorial, range(1, n + 1)) # prints 120
print reduce(factorial, range(1, n + 1), 0) # prints 0

def another_factorial(n):
    def multiply_them(a, b): return a * b
    print reduce(multiply_them, range(1, n + 1))

another_factorial(5) # prints 120
"""
"""
List comprehensions work thus:
[return something for Y in X for Z in Y if blahblah]
LEARN: nesting list comprehensions, amazing....
"""
"""
del can be used to delete variables, del variable_name, to delete objects in a list, del listname[index], or to delete list slices, del listname[x:y], del listname[:]  
"""
"""
Tuples are ordered lists, instatiated by listing all elements separated by commas, Ex:
Q = 'god', 'acid', 'cloud'
Q
>>> ('god', 'acid', 'cloud')
You can assign variables to the values in a tuple
A, B, C = Q
A 
>>> 'god'
B
>>> 'acid'
C
>>> 'cloud'
etc.

Tuples are immutable. You cannot add or take away from a tuple nor can you modify an element of a tuple.

However you can modify objects within elements of a tuple. For example:

Q = 1, 2, [3, 4]
Q[0] = 5 ERROR!
Q[2][1] = 5
Q
>>> (1, 2, [3, 5])

And you can also completely reassign a tuple
Q = 2, 3
Q 
>>> (2, 3)

Tuples can contain tuples.
An empty tuple is instatiated thus: tuple = () while a tuple with one element is instantiated thus: tuple = element,
"""
"""
A set is an unordered list with no duplicates.
It can be instantiated in two ways, 
Set = {element1, element2, etc.} , here an must be immutable: number, string, tuple.
or 
Set = set(list/string), an empty set requires the latter method. The list cannot contain other lists. If a string is entered, it will be treated as a list of chracters.

print set('abcabc')
>>> set(['a', 'b', 'c'])

Sets support mathematical set operations

Set_A - Set_B returns the elements found only in A.
set_A & Set_B returns the elements found both in A and in B.
Set_A | Set_B returns the elements found in A, B, or both.
Set_A ^ Set_B returns the elements found in only A or only B.

Set comprehensions can be done like this:
{what_you_return for x in string/list condition} Ex.

SET = set(['cats', 'dogs'])

print {x + " are the coolest" for x in SET if x != 'dogs'}
>>> set(['cats are the coolest'])

Sets cannot contain sets. Neither can they contain lists.  A set can only contain immutable objects: numbers, strings, and tuples.
You can remove objects from a set, but you cannot append objects to a set.
"""
"""
Dictionaries can use numbers, strings, or tuples as keys and any kind of object as values.

crazy_dictionary = {'cat': set(['dog', 'alien']), 'ninja': 2}
print crazy_dictionary

You can also create dictionaries like this:
dict([('key1', 'value1'), ('key2', 'value1')])
OR
dict(key1=value1, key2=value2, etc.)

Dictionary comprehension works like this:
{key: value for x in y}

print {x: x + "ly" for x in ['quick', 'slow']}
>>> {'quick': 'quickly', 'slow': 'slowly'}
"""
"""
LEARN: enumerate() what does it do? Does it return None?
Enumerate takes a list and creates a list of binary tuples (or lists?) where the first item is the index and the second is the corresponding object.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print {y: x for x, y in enumerate(alphabet)}

---

wtf = enumerate(['chicken', 'hawk'])

for x in wtf:
	print x

>>>	
(0, 'chicken')
(1, 'hawk')
"""
"""
Some code from the tutorial:

>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print i, v
...
0 tic
1 tac
2 toe
"""
"""
questions = ['name', 'quest', 'favorite color']
answers = ['damian of brooklyn', 'jenny', 'green']

for q, a in zip(questions, answers):
    print 'what is your ' + q + '? It is ' + a + "."
    
for x in zip(questions, answers):
    print 'what is your ' + x[0] + '? It is ' + x[1] + "."

zip takes lists or strings(lists of characters) and creates a list of tuples. 
LEARN: .format()
"""
"""
list.reverse() actually reverses the original list. Returns nothing
reversed(list/string) creates a reversed version of the original list in the form of tuple.

Likewise with list.sort() and sorted(list)
"""
"""
Using dictionary.iteritems() you can create list of pair tuples: [(key, value), (key, value)] etc.
"""
"""
is, is not, in, not in

a = "cat"
b = "cat"

if a in b:
    print True
else: print False

>>> True

if a is b:
    print True
else: print False

>>> True

"""
"""
From the tutorial. All the following expressions return True
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
"""
"""
Apparently this is capable of producing any of C, D, E. I always get C.

C = 'cat'
D = 'dog'
E = 'emo'

A = C or D or E
print A
"""
"""
You can convert a tuple/set/string/dict into a list using:
list(object)
"""
"""
You can straight up write
return
to break out of a function







