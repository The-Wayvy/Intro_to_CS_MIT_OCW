def product_counter(x):

	master_list = []

	for y in range(1, x + 1):
		for z in range(1, x + 1):
			if y != z:
				master_list.append(y * z)

	copy_remover = []

	for number in master_list:
		if not number in copy_remover:
			copy_remover.append(number)

	from math import sqrt

	list_of_squares = []

	for big_num in copy_remover:
		if sqrt(big_num) - int(sqrt(big_num)) == 0:
			list_of_squares.append(big_num)

	print "Two copies of", x, "produce", len(copy_remover), "unique products. Here they are:"
	print copy_remover
	print "and they also produce", len(list_of_squares), "unique perfect squares:"
	print list_of_squares

product_counter(7)
product_counter(100)
product_counter(3)

"""
Try doing this with copy_remover and square_collector as functions
"""

"""
How to deal with irrational indent error messages?
"""
