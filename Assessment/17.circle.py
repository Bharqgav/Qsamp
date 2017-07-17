import sys
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print "The area is", 3.14*((self.radius)**2)
a = int(raw_input("enter radius"))
R = Circle(a)
R.area()
