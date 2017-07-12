import sys
print"* "*5
for b in range(10):
    if (b < 6):
        print"* "
    elif (b == 6):
        print"* "," "*2,"* "*2
    elif (b == 9):
        print"* "*5
    else:
        print"* "," "*4,"* "
