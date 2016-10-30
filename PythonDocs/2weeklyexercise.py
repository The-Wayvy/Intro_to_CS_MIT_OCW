counter = 99

while counter > 2:
	print "%s bottles of beer on the wall, %s bottles of beer, take 1 down, pass it around," % (counter, counter), (counter - 1), "bottles of beer on the wall."
	counter -= 1 
else:
	if counter == 2:
		print "2 bottles of beer on the wall, 2 bottles of beer, take one down, pass it around, 1 bottle of beer on the wall." 
		print "one bottle of beer on the wall, one bottle of beer, take it down, pass it around, we are drunk as fuck!"

"""
CHECK!
"""


"""
Remember, you can print different types of objects on the same line by separating them with commas. The comma also creates whitespace.
"""