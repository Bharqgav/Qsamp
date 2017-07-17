import sys
try:
    a = float(raw_input("enter a number"))
    if not ((a).is_integer() or a>=0):
        print("Sorry!")
    else:
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
except ValueError:
    print("Enter numbers!")
