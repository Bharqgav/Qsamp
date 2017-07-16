#reverse string
import sys
a = raw_input("enter a string")
reverse = a[len(a) - 1]
for b in range(0,len(a)-1):
    reverse = reverse + a[len(a) - b - 2]
    
print reverse
