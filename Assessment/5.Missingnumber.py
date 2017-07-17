import sys
a = raw_input("Enter a list of numbers ")
b = a.split()
for i in range(len(b)):
    if not i == len(b) - 1:
        if not int(b[i]) + 1 == int(b[i+1]):
            print i + 2
