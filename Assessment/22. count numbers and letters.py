import sys
a = raw_input("Enter a string")
x = 0
y = 0
for char in a:
    if char.isdigit():
        x = x+1
    elif char.islower() or char.isupper():
        y = y+1
    
print "Numbers :", x
print "Letters :", y
