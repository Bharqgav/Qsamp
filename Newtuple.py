import sys
tup = [1,2,3,4,5,6,7,8,9,10]
t = list()
for b in range(0,len(tup)):
    if not tup[b] % 2 == 0:
        t.append(tup[b])
print tuple(t)
