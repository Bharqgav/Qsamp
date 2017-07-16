#Please write a program which prints all permutations of [1,2,3]
import sys
thelist = int(raw_input("Enter three numbers "))
a = thelist[0]
b = thelist[1]
c = thelist[2]

for a  in thelist:
    for b in thelist.remove(a):
        for c in thelist.remove(a,b):
            print a, b, c




