def print_factors(x):
	LOF = []
	for y in range(1, x+1):
		if x % y == 0:
			LOF.append(y)
	print LOF

"""
CHECK
"""