import sys

x = int (raw_input("Enter the height "))
y = int (raw_input("Enter the breadth "))
if x < 4 or y < 3 :
    print ("sorry, please enter height values greater than 3 and breadth values greater than 2")
else:
    print"* "*y

    for b in range(x-1):
     
        if(x % 2 == 0):
            if (b == x/2 - 1):
                print"* "*y
            else:
                print"* "+" "*(2*y-4)+"* "
        else:
            if(b == (x-1)/2 - 1):
                print"* "*y
            else:
                print"* "+" "*(2*y-4)+"* "

