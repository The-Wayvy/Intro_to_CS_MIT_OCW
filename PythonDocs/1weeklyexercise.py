master_list = range(1, 1000, 2)

even_reversed = range(1000, -1, -2)


for number in even_reversed:
	master_list.append(number)
else: print master_list


"""
CHECK!
"""

"""
Note: append modifies a list and returns None

