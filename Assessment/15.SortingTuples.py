import sys
from operator import itemgetter
a = [(1,2,3),(4,5,6),(3,5,2),(9,1,0)]


b = sorted(a, key=itemgetter(-1))
print b
