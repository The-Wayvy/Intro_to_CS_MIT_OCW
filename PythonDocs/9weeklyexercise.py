class Triangle(object):

	def __init__(self, name, side_one, side_two, side_three):
		self.name = name
		self.side_one = side_one
		self.side_two = side_two
		self.side_three = side_three
		
	def what_kind(self):
		if self.side_one == self.side_two == self.side_three:
			return "Equilateral"
		elif self.side_one == self.side_two or self.side_two == self.side_three or self.side_three == self.side_one:
			return "Isoscles"
		else: return "Scalene"

	def perimeter(self):
		Per = self.side_one + self.side_two + self.side_three
		return Per	


	def area(self):
		import math
		half_per = self.perimeter() / 2
		Area = math.sqrt(half_per * (half_per - self.side_one) * (half_per - self.side_two) * (half_per - self.side_three))
		return Area

	def bigger(self, new_triangle):
		if self.area() > new_triangle.area():
			print self.name + " is bigger"
		elif self.area() == new_triangle.area():
			print "They're equal in size."
		else: print new_triangle.name + " is bigger."


Original_Triangle = Triangle("Mr. T", 3, 4, 5)

Original_Triangle.bigger(Triangle('damian', 12, 13, 18))  

print Original_Triangle.area()

"""
Note: objects can serve as arguments.
"""
