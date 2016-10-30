"""
Project Euler Problem 7
Find the 10th prime
"""


def finder():
    """Return the 10th prime number"""
    p = 2
    n = 1
    while n < 10:
        p += 1
        if is_it_prime(p):
            n += 1
        else: pass
    else: return p

def is_it_prime(x):
    """Returns True if (x) is prime and False otherwise"""
    for num in range(2, x):
        if x % num == 0:
            return False
    else: return True


print finder()

"""
you can also make a list of primes and check its length

BE MORE FUCKING CAREFUL AND THEN YOU WONT HAVE TO BE AS PATIENT!!!

When code doesn't work, test each individual function.
"""
