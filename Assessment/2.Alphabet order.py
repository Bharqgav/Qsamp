import sys
a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']
for i in range(4):

    print ''.join(a[:i+1])
    for b in range(i+1):
        a.pop(0)
