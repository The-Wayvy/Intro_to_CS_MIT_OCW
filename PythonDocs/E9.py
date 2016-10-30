"""
Project Euler Problem 10
Find the sum of primes smaller than 30 (X)
"""

import E0

def is_prime(y):
    """Return True if a number is prime, false otherwise"""
    for num in range(2,y):
        if y % num == 0:
            return False
    else: return True

def find_sum_primes(x):
    """Sum the prime numbers between 2 and x"""
    total = 0
    for z in range(2,x+1):
        if is_prime(z):
            total += z
    else: print total

#print __name__
#This returns __main__

if __name__ == "__main__":
    import sys
