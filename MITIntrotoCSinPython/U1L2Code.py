##x = 3  #Create variable x and assign value 3 to it
##x = x*x  #Bind x to value 9
##print x
##y = raw_input('enter a number:')
##print type(y)
##print y
##y = float(raw_input('Enter a number: '))
##print type(y)
##print y
##print y*y
##
##x = int(raw_input('Enter an integer: '))
##if x%2 == 0:
##    print 'Even'
##else:
##    print 'Odd'
##    if x%3 != 0:
##        print 'And not divisible by 3'
##
##x = int(raw_input('Enter x: '))
##y = int(raw_input('Enter y: '))
##z = int(raw_input('Enter z: '))
##
##
##if x < y:
##    if x < z:
##        print 'x is least'
##    else:
##        print 'z is least'
##elif y < z:
##    print 'y is least'
##else:
##    print 'z is least'  
##
##if x < y and x < z:
##    print 'x is least'
##elif y < z:
##    print 'y is least'
##else:
##    print 'z is least'
##    
##
###Find the cube root of a perfect cube
#x = int(raw_input('Enter an integer: '))
#ans = 0
#while ans*ans*ans < abs(x):
#    ans = ans + 1
#    print 'current guess =', ans
#if ans*ans*ans != abs(x):
#    print x, 'is not a perfect cube'
#else:
#    if x < 0:
#        ans = -ans
#    print 'Cube root of ' + str(x) + ' is ' + str(ans)
##
##
##if x == y:
##    print 'yes'
##else:
##    print 'no'
# This whole thing is a branching program but it contains 3 straightline programs

##if x == y:
##    print 'yes'
##else:
##    print 'no'
##if x == y:
##    print 'yes'
##else:
##    print 'no'
##if x == y:
##    print 'yes'
##else:
##    print 'no'
### This whole thing is a straight line program composed of 3 branching programs
##
##if x == y:
##    print 'ohm'
##elif: x > y:
##    print 'boo'
##else:
##    print 'yay'
### is the same thing as
##if x==y:
##    print 'ohm'
##else:
##    if x > y:
##        print 'boo'
##    else:
##        print 'yay'

### return the largest odd number
##
### Since we have fixed the number of inputs this function runs in constant time
### It can at most test 2**3 == 8 cases.
##
# Case 1: x is odd, y is odd, z is odd. Case 2: x is odd, y is odd, z is even.
x = 1
y = 2
z = 3
if x % 2 == 1 and y % 2 == 1:
    if x > y:
        if z % 2 == 1:
            if x > z:
                print x
            else:
                print z
        else:
            print x
    else:
        if z % 2 == 1:
            if y > z:
                print y
            else:
                print z
        else:
            print y
# Case 3: x is odd, y is even, z is odd
elif x % 2 == 1 and z % 2 == 1:
    if x > z:
        print x
    else:
        print z
# Case 4: x is even, y is odd, z is odd
elif y % 2 == 1 and z % 2 == 1:
    if y > z:
        print y
    else:
        print z
# Case 5: x is odd, y is even, z is even
elif x % 2 == 1:
    print x
# Case 6: x is even, y is odd, z is even
elif y % 2 == 1:
    print y
# Case 7: x is even, y is even, z is odd
elif z % 2 == 1:
    print z
# Case 8: x is even, y is even, z is even
else:
    print "nada"

# Take ten integers and print the largest odd one
##x = 0
##count = 10
##while count > 0:
##    y = int(raw_input(str(1337) + "forever: "))  
##    if x == 0 and y % 2 == 1:
##        x = y
##        count -= 1
##    elif y > x and y % 2 == 1:
##        x = y
##        count -= 1
##    else:
##        count -= 1
##else:
##    if x % 2 == 1:
##        print x
##    else:
##        print 'no odd numbers were entered'
