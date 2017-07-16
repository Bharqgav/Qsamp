import sys
data = []
while True:
     a = raw_input("Enter data ")
  
     if not a: break
     
     data.append(a)
print data
x = 0
for i in data:
    c = i.split()
    if c[0] == 'D':
        x = x+ int(c[1])
    elif c[0] == 'W':
        x = x- int(c[1])
    else:
        print("Invalid Data")
        break

print x
