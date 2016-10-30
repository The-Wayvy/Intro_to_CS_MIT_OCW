"""
Euler Problem 9
There exist a, b, c such that a + b + c = 1000 and a**2 + b**2 = c**2
Find abc
"""
"""
Create a list of possible c values, 335 to 499
Then two lists for possible a/b values, 167 to 498 # you can calc these values
Create a function to test if a, b, c are a pythag trip
"""

for c in range(5, 40):
    for b in range(4, c+1):
        for a in range(3, b+1):
            if a + b + c == 40 and c**2 == b**2 + a**2:
                print a, b, c, "product:", a*b*c
