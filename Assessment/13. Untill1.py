import sys
a = int(raw_input("enter a number"))
b = []
b.append(a)
while True:
    if a == 1:
        print b
        break
    elif a%2 == 0:
        b.append(a/2)
        a = a/2
    else:
        b.append(3*a + 1)
        a = 3*a +1
