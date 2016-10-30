"""
Euler Problem 3
Find the largest prime factor of X
Python runs out of memory on the original request
"""

"""
Divide the list in half
Go through it in reverse order
Return the first prime factor
"""

def prime_tester(a):
    """Return False if (a) isn't prime and True if (a) is prime"""

    for b in range(2, a/2 + 1):
        if a % b == 0:
            return False
    else: return True


def factor_harvester(x):
    """Find the largest prime factor of x
        First find a factor, then test primeness"""

    y = x / 2
    for z in range(y, 1, -1):
        if x % z == 0:
            if prime_tester(z):
                print z
                break
    else: print "no prime factors"

factor_harvester(14)
    
