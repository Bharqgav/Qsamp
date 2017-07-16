import sys
a = raw_input("Enter a sentence ")
x = list()
y = 0
for char in a:
    if char.isdigit():
        x.insert(y, char)
        y = y + 1
print x
