"""
Project Euler Problem 8
Find the X consecutive digits with the largest product in a Y digit number.
"""

"""
Turn the number into a list of number strings.
Create a list of 4-conescutive-digit numbers
"""

def sum_comparison(a, b): return a if summing_lists(a) > summing_lists(b) else b 
"""Return the list whose sum is greater"""
def summing_lists(q):
    """Return the sum of the integers represented by a list of strings"""
    total = 0
    for stringer in q:
        total += int(stringer)
    return total

def create_list(x):
    """Turn an integer, x, into a list of the integer digits as strings
        Then Create a list of all possible 4-consec digit lists"""
    da_digits = list(str(x))
    copy_of = da_digits[:]
    candidates = []
    while len(copy_of) > 3:
        candidates.append(copy_of[0:4])
        del copy_of[0]
    return candidates

#print create_list(1234567)
#print summing_lists(['2', '3', '4', '5'])
#print sum_comparison(['2', '3', '4', '5'], ['7', '1', '8', '6'])
print reduce(sum_comparison, create_list(292999918))
