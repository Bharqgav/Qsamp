import sys
a = raw_input("please input your email")
b = list(a)
c = b.index('@')
d = b.index('.')
print ''.join(b[c+1:d])
