"""def Fibonacci(n):
        fibs = []
        for num in range(n + 1):
                if num == 0:
                        fibs.append(num)
                elif num == 1:
                        fibs.append(num)
                else:
                        fib = fibs[num - 2] + fibs[num - 1]
                        fibs.append(fib)
        else:
                print "Here they are!", fibs[1:]

        clean_fibs = fibs[1:]

        if len(clean_fibs) > 2:
                print "The 1st fibonacci number is", 1
                print "The 2nd fibonacci number is", 1
                for numb in clean_fibs[2:]:
                        repre = str(clean_fibs.index(numb) + 1)
                        last = repre[len(repre) - 1]
                        if (last == '0' or last == '4' or last == '5' or last == '6' or last == '7' or last == '8' or last == '9'):
                                print "The " + repre + "th fibonacci number is", numb
                        elif last == '3':
                                print "The " + repre + "rd fibonacci number is", numb
                        elif last == '2':
                                print "The " + repre + "nd fibonacci number is", numb
                        else: print "The " + repre + "st fibonacci number is", numb
        elif len(clean_fibs) == 2:
                print "The 1st fibonacci number is", 1
                print "The 2nd fibonacci number is", 1
        else:
                print "The 1st fibonacci number is", 1

Fibonacci(35)
"""
        
        
"""
The issue is that list.index(value) always returns the lowest index which has that value.
"""
"""
What would I do if I had a list with lots of repetition and I wanted to label each
number the way I did here?
"""

def fib(n):
        a = 0
        b = 1
        count = 1
        while count <= 10:
                count += 1
                print b
                a, b = b, a+b

fib(10)
