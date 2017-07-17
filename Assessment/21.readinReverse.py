import sys
for line in reversed(open("myfile.txt").readlines()):
    print line.rstrip()
