import sys


def Add(x, y):
        c = 0    
        for char in x :
            
            if not char.isdigit():
                c = 1
                break
       
        for char in y :
            d = 0
            if not char.isdigit():
                d = 1
                break
        if c == 1 or d == 1:
             return "Invalid"
        else:
             return float(x) + float(y)

def Subtract(x, y):
        c = 0    
        for char in x :
            
            if not char.isdigit():
                c = 1
                break
       
        for char in y :
            d = 0
            if not char.isdigit():
                d = 1
                break
        if c == 1 or d == 1:
             return "Invalid"
        else:
             return float(x) - float(y)

def Product(x, y):
        c = 0    
        for char in x :
            
            if not char.isdigit():
                c = 1
                break
       
        for char in y :
            d = 0
            if not char.isdigit():
                d = 1
                break
        if c == 1 or d == 1:
             return "Invalid"
        else:
             return float(x) * float(y)

def Division(x, y):

     
        c = 0    
        for char in x :
            
            if not char.isdigit():
                c = 1
               
       
        for char in y :
            d = 0
            if not char.isdigit():
                d = 1
                
        if c == 1 or d == 1:
             return "Invalid! Enter a number"
             
        elif float (y) == 0:
             return "Invalid! Second number can't be zero"
        else:
             return float(x) / float(y)




x = raw_input("Enter a number ")
y = raw_input("Enter another number ")


while True:

    z = raw_input("Enter an operation from Add/Subtract/Product/Division ")

    if z == "Add":
        print Add(x,y)
        break
    elif z == "Subtract":
        print Subtract(x,y)
        break
    elif z == "Product":
        print Product(x,y)
        break
    elif z == "Division":
        print Division(x,y)
        break
    else:
        print ("Invalid! ")



