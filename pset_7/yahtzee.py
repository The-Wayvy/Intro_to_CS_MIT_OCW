# should be 1 / 6**4
# there are 6**5 possible rolls
# 6 of them are yahtzees
# all rolls are equally likely

import random

sides = [side / 6.0 for side in range(1,7)]

def is_less_than(x):
	"""
	x: float
	y: list of floats

	returns the number of values in y greater than x
	""" 
	return 1 + sum([x < value for value in sides])

is_yahtzee = 0
for trial in range(100000):
	rolls = [random.random() for roll in range(5)]
	outcomes = map(is_less_than,rolls)
	if outcomes[0] == outcomes[1] and outcomes[0] == outcomes[2] and outcomes[0] == outcomes[3] and outcomes[0] == outcomes[4]:
		is_yahtzee += 1 

print "experimental probability:", is_yahtzee / 100000.0
print "theoretical probability:", 1.0 / 6**4