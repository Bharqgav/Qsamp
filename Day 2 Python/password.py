import sys
a = sys.argv[1]
b = 0
if (len(a)>5 and len(a) <17):
    
    for b in range (0,len(a)+1):
        if (a[b] == '&') or (a[b] == '%') or (a[b] == '@') :
            print("valid")
            break
else:
    print("Invalid")
        
