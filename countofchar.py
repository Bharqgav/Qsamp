import sys
a = raw_input("Enter a string")
norepeat = ''
for char in a:
    x = 0
    b = char.lower()
   
    for char in a:
        
        if char.lower() == b.lower():
            x = x+1
    if not b in norepeat:
        print b, x
    norepeat = b + norepeat
