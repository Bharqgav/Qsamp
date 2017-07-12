import sys
city = {"mumbai" : "maharashtra", "pune" : "maharashtra", "nasik" : "maharashtra"}

while True:
    name = raw_input()
    if name.lower() in city:
         print city[name.lower()]
         break
    elif name.lower() in city.values():
         print city.keys()[city.values().index(name.lower())]
         break
    else:
         print "error"
