import sys
class Circle:
    def __init__(self):
        a = raw_input("enter string")
        self.string = a
    def area(self):
        print "The string is", self.string

n = Circle()
n.area()
