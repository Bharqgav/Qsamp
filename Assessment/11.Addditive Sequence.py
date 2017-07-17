import sys
try:
    a = raw_input("Enter a sequence of numbers")
    b = map(int, a.split())
    for i in range(2,len(b)):
        
        if not b[i] == (b[i-1] + b[i-2]):
            
            print "Not a sequence"
            break
        elif i == len(b)-1:
            print "It's an addition sequence"
            
except ValueError:
    print("oops! Enter a number")
