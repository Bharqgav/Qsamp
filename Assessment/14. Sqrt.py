import sys

try:
        
        a = int(raw_input("enter a number"))

        b = a**(.5)

        if (b).is_integer():
                print("The number is a power of two.")
        else:
                print("The number is not a power of two.")

except ValueError:
        print("Err...enter positive numbers")
