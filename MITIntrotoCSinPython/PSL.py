##x = ''
##y = input('enter a number or "done" if you\'re done: ')
##while y != 'done':
##    if x == '' and y % 2 == 1:
##        x = y
##        y = input('enter a number or "done" if you\'re done: ')
##    elif y % 2 == 1 and y > x:
##        x = y
##        y = input('enter a number or "done" if you\'re done: ')
##    else:
##        y = input('enter a number or "done" if you\'re done: ')
##else:
##    if x == '':
##        print "you didn't enter any odd numbers"
##    else:
##        print x, "is the largest odd number you entered"
        
# A long integer is a type of number used to represent integers larger than
# the largest integer type supported by your machine

# all(iterable) returns True if the iterable is empty or contains all Trues
# any(iterable) returns True if at least one item in the iterable is True.
##print all((True, True, 4))
##print all([])
##print all([False, True])
##print any('cat')
##print any((False, True))
##print any(())

# isinstance(object, type) is equivalent to: type(object) == type
# it can also take a tuple of types/classes
# basestring is a super class for strings and unicode
##print isinstance(3,int)
##print isinstance('cat', basestring)

# cmp(x,y) returns -1 if x>y, 0 if x ==y, and 1 if x < y
##print cmp(1, 2), cmp(2,1), cmp(1,1)

# you can create a dictionary thus: dict(list of binary tuples)
##x = dict([(1,'cat'),(2,'dog')])
##print x 
##print dir(x)
##x.__delitem__(1)
##print x
##print x.get(1,'squirrel')

# delattr(object, method) deletes an object's method. getattr returns it
# hasattr returns a boolean

# divmod(a, b) returns the quotient and remainder in a tuple
##print divmod(7.9,2.5)

# enumerate(iterable, start=0) takes an iterable and returns an X of binary
# tuples of the form (index, item) with index starting at start.
# the x must be specified thus: type(enumerate(iterable, start=0))
##name = "Damian"
##A = dict(enumerate(name))
##print A
##B = list(enumerate(name,1))
##print B
##c = {'q': 'cat', 'z': 'dog'}
##C = set(enumerate({'q': 'cat', 'z': 'dog'},1))
##print C

# filter(function, iterable) returns (by default a list) an iterable composed
# of elements of the iterable that evaluate to False in the function
# if None is used as the function then the function becomes identity
# So the function must return a boolean
# Similar to list comprehension [item for item in iterable if function(item)]
# Here function must return a boolean
##def positive(x):
##    if x > 0:
##        return True
##print filter(positive,[-1, 0, 1, 2])
##print [x for x in [-1,0,1,2] if positive(x)]
##print [x for x in [-1,0,1,2] if x > 0]

# map(function, iterable, ...) applies function to every item in iterable.
# The function must take as many arguments as there are literals.
# None is substituted for non-existant values when one iterable is shorter
# If no function is entered the identity function is applied

##def largest(z, y, x):
##    return max([z,y,x])
##print map(largest,[1,5,2,5],[5,2,6],[1,9,4])
#Note, you cannot perform operations on None
##print map(None,[1,5,2,5],[5,2,6],[1,9,4])
#Transpose hack
##def is_num(x):
##    if type(x) == int:
##        return True
##    else:
##        return False
##print map(is_num,[1,2,'a'])



##import math
##print math.sqrt(25)
##print getattr(math,'sqrt')(25)

#globals() returns all global variables and functions
#locals() returns variables that are native to the current scope.

##SHFKSJFDGFKDJFHKJHFKGSDKFHSKDFJH = 848745354
##def wtf(a,b,c):
##    hkdfjhskdfhsdfhsx = sum([a,b,c])
##    print globals()
##wtf(4,2,9)
##print globals()

##import math
##print hasattr(math,'sqrt') # this returns true

#hash(object), turns a number/string/boolean into an integer. k...

#help('word') will provide resources on a subject, function, module, etc.

# id(object) returns an objects location in memory

# int(string,base) converts a number string of base x to decimal

# issubclass(class, classinfo) returns true if class is a subclass of any of the
# class in classinfo

##def bunny(r, s):
##    Q = r + s
##    print globals()
##    print locals()
##bunny(2, 8)
##print globals()
##print locals()

# min and max work on both iterables and literals separated by commas

# object() is used to assign a name to a blank object.

# pow(x,y[,z]) = x**y is z isn't supplied and (x**y)%z if it is. for latter y>0

# 

#???Nonintuitive True/False evaluations Ex. 3 evaluates to true but 3 != True???????
#???Boolean is a subclass of int??? Like 1 and 0. Why does bool([x]) exist???
#???Bytes,unicode,ascii,AST,etc.???
#delattr(object, name) and setattr(object, name)
#figure out yield
#files...input/output etc.
#???yield??? the fuck?
#??? iter(o[,sentinel]) creates an iterator???
#next(iter,[default]) coughs up one value at a time, default after exhaustion
#???What are frozen sets good for???
#???List Comprehension with map/reduce???
#???Optional 'key' argument in max???
#???Memory View???
