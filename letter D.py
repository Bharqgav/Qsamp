import sys
x = int (raw_input("Enter the height "))
y = int (raw_input("Enter the breadth "))

if x < 3 or y < 2 :
    print ("sorry, please enter height values greater than 3 and breadth values greater than 2")
else:
    print"* "*y
    for a in range(x-2):
        print"* "+" "*(2*y-3)+"*"
    print"* "*(y)
    

