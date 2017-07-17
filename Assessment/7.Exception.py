class Error(Exception):
 
   
    def __init__(self, value):
        self.value = value
 
    
    def __str__(self):
        return(repr(self.value))
 
try:
    raise(Error(3*2))
 

except Error :
    print('A New Exception occured: ',Error.value)
