#Please write a program which accepts a string from
#console and print the characters that have even indexes.
import sys
a = raw_input("Enter a string ")
even = a[0]
b = 2
for b in range(2,len(a)):
    if b%2 == 0:
        even = even+a[b]
print even
