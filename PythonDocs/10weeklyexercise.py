class Gradebook(object):
    def __init__(self, number):
        self.number = number

    def letter(self):
        if self.number >= 90:
            return 'A'
        elif self.number >= 80:
            return 'B'
        elif self.number >= 70:
            return 'C'
        elif self.number >= 60:
            return 'D'
        else: return 'F'

print Gradebook(25).letter()
print Gradebook(75).letter()
print Gradebook(95).letter()
