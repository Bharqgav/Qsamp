import sys

def coloredprint(text,color):
    if color == 1:
        print(text,color,'red')
    if color == 2:
        print(text,color,'green')
    else:
        print "colored print function: color argument", color, "is not a viable argument, specify 1 or 0"
        raise RuntimeError
text = raw_input("Enter text")
color = raw_input("Enter color")
coloredprint(text,color)
