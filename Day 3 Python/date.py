

import sys


while True:
    year = int (raw_input("Input a year: "))
    month = int (raw_input("Input a month: "))
    day = int (raw_input("Input a day: "))
    
    if month > 0 and month <13 and day>0 and day<31 and year >0:
        print"The next date is {}-{}-{}". format(year, month, day+1)
        break
    elif month > 0 and month <12 and day>0 and day == 31 and year >0:
        print"The next date is {}-{}-{}". format(year, month+1, 01)
        break
    elif month > 0 and month ==12 and day>0 and day == 31 and year >0:
        print"The next date is {}-{}-{}". format(year + 1, 01,01)
        break
    else:
        print"Sorry!"
    
