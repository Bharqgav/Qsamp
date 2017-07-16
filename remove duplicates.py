#Define a class Person and its two child classes: Male and Female.
#All classes have a method "getGender" which can print "Male" for
#Male class and "Female" for Female class.

import sys
a = raw_input("Enter a list of numbers")
c =  a.split()
print c
d = list()
for b in c:
       if  b not in d:
        d.append(b)
print d[::-1] #Syntax for reversing the list

