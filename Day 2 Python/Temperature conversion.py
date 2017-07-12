import sys
a = float(sys.argv[1])
b = sys.argv[2]

if (b == "c"):
    print (a * 1.8) + 32, 'f'
elif (b == "f"):
    print (a - 32)* 0.555, 'c'
else:
    print("sorry")