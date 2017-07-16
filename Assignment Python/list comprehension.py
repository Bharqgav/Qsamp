#list comprehension
import sys
a = raw_input("Enter a list of numbers")
c = a.split() #storing the string input as a list 
l = [] #Creating an empty list

b = [0,2,4,6]
for i in b:
         c.remove(c[i])
         c.insert(i," ") #replacing the removed numbers with spaces so that the inex count does not change
for x in c:
    if not x==" ": #To create a list without the spaces created to replace the numbers which are to be removed
        l.append(x)
print l

#Alternate code

import sys
a = raw_input("Enter a list of numbers")
c = a.split() #storing the string input as a list 
l = [] #Creating an empty list

b = [0,1,2,3] #counting the indexes inorder to remove 0,2,4,6th elements
for i in b:
         c.remove(c[i])
         
    
print c
