import sys
b = raw_input("Enter a string ")
with open("myfile.txt", "a") as myfile:
        myfile.write( b)
