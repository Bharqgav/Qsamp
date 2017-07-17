import sys
class List:
   def __init__(self,elements):
       self.elements = elements

   def append(self,x):
       self.elements.append(x)

   def delete(self,x):
       try:
           self.elements.remove(x)
       except ValueError:
           print("given value is not present in the list")

   def display(self):
       print self.elements


a = raw_input("Enter a list")
b = a.split()
l = List(b)
l.append(7)
l.display()
l.delete(7)
l.display()
