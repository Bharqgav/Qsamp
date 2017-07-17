import sys
a = raw_input("Enter a string")
norepeat = '' #Empty string
l = []
for char in a:
    x = 0
    b = char.lower() #This assumes if the string has an upper and lower case of same letter then it is counted as a repeat
   
    for char in a:
        
        if char.lower() == b.lower(): #to find if b repeats
            x = x+1 #x returns the number of times char apperas
    if not b in norepeat:
        print b, x
    norepeat = b + norepeat #If a character is appearing more than once, then it appears only once
