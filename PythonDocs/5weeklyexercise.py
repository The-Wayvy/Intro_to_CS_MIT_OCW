def manipulate(*args):
	product = 1
	for a_list in args:
		if a_list == []:
			product = 0
			break
		else: 
			summ = sum(a_list)
			if summ == 0:
				product = 0
				break
			else:
				product *= summ
	print product

"""
Remember: if a for-loop is broken, its else statement is still executed.
"""


"""
CHECK
"""