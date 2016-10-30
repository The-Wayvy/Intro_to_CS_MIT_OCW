"""
Project Euler Problem 8
Find the difference of the square of the sum of 1 to 100 and the sum of the
squares of 1 to 100
"""


sum_of_squares = sum([x**2 for x in range(1,101)])

square_of_sum = sum(range(1,101))**2

print square_of_sum - sum_of_squares
