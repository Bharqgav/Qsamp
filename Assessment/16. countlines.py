import sys
#a = raw_input("Enter text")
#b = a.split('.')
#print len(b)

print sum(1 for line in open('myfile.txt'))
