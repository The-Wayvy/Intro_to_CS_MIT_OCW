"""
Project Euler Problem 1
Sum the multiples of 3 and 5 smaller than 1000
"""

def three_mults():

    """List all positive multiples of 3 less than 1000"""

    three_list = []
    n = 2
    x = 3
    while x < 1000:
        three_list.append(x)
        x = n * 3
        n += 1
    return three_list


def five_mults():

    """List all positive multiples of 5 less than 1000"""

    five_list = []
    x = 5
    n = 2
    while x < 1000:
        five_list.append(x)
        x = n * 5
        n += 1
    return five_list

total = set(three_mults() + five_mults())
print sum(total)
        
        

