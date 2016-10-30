class Circle(object):

    pi = 3.14

    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

    def area(self):
        Area = self.pi * self.radius ** 2
        return Area

    def circumference(self):
        Circumference = 2 * self.pi * self.radius
        return Circumference

    def vol_alpha_sphere(self):
        Volume = 4 / 3 * self.pi * self.radius ** 2
        return Volume

def compare_balls(*args):
    null_ball = Circle('not a ball', 0)
    biggest = null_ball
    for ball in args:
        if ball.vol_alpha_sphere() > biggest.vol_alpha_sphere():
            biggest = ball
    else: print 'The biggest ball is ', biggest.name
    
A_Ball = Circle('Joseph', 7)
B_Ball = Circle('Andrew', 3)

print compare_balls(A_Ball, B_Ball)

"""
CHECK
"""

"""
Why the fuck does pi need to be defined outside the class?
I'm using it only for class objects.
"""

"""
Figured it out.
Although I think of pi as a variable, it isn't.
pi is a method that returns a value 
HENCE
self.pi
NOT
pi
""""
