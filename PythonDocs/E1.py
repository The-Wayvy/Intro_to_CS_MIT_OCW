""""
Project Euler Problem 2
Find the sum of even fibonacci numbers less than 4,000,001
"""

def fib_even():

    """ Creates a list of even fibonacci numbers"""

    a, b = 1, 2
    master_list = []
    while a <= 4000000:
        if a % 2 == 0:
            master_list.append(a)
            a, b = b, a + b
        else: a, b = b, a + b
    else: return master_list

print sum(fib_even())


