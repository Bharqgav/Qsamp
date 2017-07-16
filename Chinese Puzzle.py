#Write a program to solve a classic ancient Chinese puzzle: 
#We count 35 heads and 94 legs among the chickens and rabbits in a farm.
#How many rabbits and how many chickens do we have?

import sys
a = int(raw_input("Enter no.of heads "))
b = int(raw_input("Enter no. of legs "))

if isinstance(a, (int, long)) and isinstance(b, (int,long)):
    if (b >= 2*a) and (4*a>=b):
        print "No. of rabbits = {}".format(b/2 - a)
        
        print "No. of chickens = {}".format(2*a - b/2)
    else :
        print "sorry! Not possible"
        
else:
        
        print("Sorry! Enter an integer")
