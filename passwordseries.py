import sys
a = raw_input("Enter a series of passwords seperated by comma")
b = map(str ,a.split(','))
l = []
def hasnum(s):
    return any(i.isdigit() for i in s)
def haslower(s):
    return any(i.islower() for i in s)
def hasupper(s):
    return any(i.isupper() for i in s)
def haschar(s):
    for i in s:
        if (i == '%' or i == '&' or i == '@'):
            return True
            break
        elif i.index == len(s)-1:
            return False


print b
for i in b:
    if  len(i) > 5 and len(i) < 13 and hasnum(i) and haslower(i) and hasupper(i) and haschar(i):       
        
            
                    l.append(i)



print (','.join(l))
  
    
            
       
