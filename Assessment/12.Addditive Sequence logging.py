import sys
import logging
try:
    a = raw_input("Enter a sequence of numbers")
    b = map(int, a.split())
    for i in range(2,len(b)):
       
        if not b[i] == (b[i-1] + b[i-2]):
            
            logging.info( 'Not a sequence')
            break
        elif i == len(b)-1:
            logging.info( 'It is an addition sequence')
            
except ValueError:
    print("oops! Enter a number")
