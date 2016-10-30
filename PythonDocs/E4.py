"""
Project Euler Problem 5
What is the smallest positive number evenly divisible by each integer from 1 to 20
"""

factors_removed = []

kept_factors = []

def factors(x):
    """ Puts x in a list and puts x's factors in another list
    """
    for y in range(2, x):
        if x % y == 0:
            factors_removed.append(y)
    kept_factors.append(x)
#
original_list = range(4, 1, -1)
"""Remove all factors of numbers in a given list"""
for x in original_list:
    if x not in factors_removed:
        factors(x)

print kept_factors
print factors_removed

def finder():
    """Finds the smallest value for which all of kept_factors members are factors.
    """
    kept_factors.sort()
    small = kept_factors[0]
    n = 2
    while True:
        value = n * small
        for nums in kept_factors:
            if value % nums != 0:
                n += 1
                break
        else: return value
# I like this :)    

print finder()

"""
removed_factors = []
kept_factors = []

for x in range(2, 21):
    for z in range(x + 1, 21):
        if z % x == 0:
            removed_factors.append(x)
            break
    else: kept_factors.append(x)

print kept_factors
"""


