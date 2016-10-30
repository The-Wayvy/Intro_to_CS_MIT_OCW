"""
Euler Probem 4
Find the largest palindromic number produced by the product of two 3-digit numbers
"""

"""
~ Get all three digit by three digit products
~ Get the palindromes
~ Get the largest
"""

def returner(b, c):
    """Return the number that is not smaller"""

    if b > c:
        return b
    else: return c

    
def palindrome(x):
    """Return True if the number is palindromic, False otherwise"""
    
    forward_list = list(str(x))
    backward_list = list(reversed(str(x)))
    if forward_list == backward_list:
        return True
    else: return False


def three_dig_prods():
    """Create a list of palindromes. Find the largest."""
    
    list_of_palindromes = []
    for x in range(99, 9, -1):
        for y in range(99, 9, -1):
            z = x * y
            if palindrome(z):
                list_of_palindromes.append(z)
    else: print reduce(returner, list_of_palindromes)

three_dig_prods()


"""
You're calculating many mirror products, 999 * 998 and 998 * 999, for example
How do we avoid this?
"""


"""
reversed(string) works on strings. It creates a tuple. But it doesnt return anything worth using
string.reverse() does not work.
list.reverse() reverses the list but returns None
"""
