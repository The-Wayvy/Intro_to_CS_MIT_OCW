"""
while 1 == 1:
    pass
"""

"""
Find the cube root of a number, if it exists.
"""

x = int(raw_input('enter a number'))

guess = 0

while guess ** 3 < abs(x):
    guess += 1
    print 'current guess:', guess

else:
    if guess ** 3 != abs(x):
        print x, 'does not have a perfect cube root.'
    elif x > 0:
        print 'the cube root of',x,'is',guess
    else: print 'the cube root of',x,'is',-guess
