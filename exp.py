#class Person:
 #   def say_hi(self): #method
#        print('Hello, how are you?')

#p = Person() #p is an object
#p.say_hi()

"""class Person:
    def __init__(self, name, aim):
        self.name = name
        self.aim = aim

    def say_hi(self):
        print('Hello, my name is', self.aim)

p = Person('Swaroop', 'fuck')
p.say_hi()"""

"""class Robot:
    """"""

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """"""
        self.name = name
        print("(Initializing {})".format(self.name))

        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def die(self):
        """"""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        """#Greeting by the robot.

        #Yeah, they can do that."""
        #print("Greetings, my masters call me {}.".format(self.name))"""

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

"This would create first object of Employee class"
a = raw_input("Enter details of emp1 ")
b = raw_input("Enter details of emp2 ")
c = a.split()
d = b.split()
emp1 = Employee(c[0], c[1])
"This would create second object of Employee class"
emp2 = Employee(d[0], d[1])
emp1.displayEmployee()
emp2.displayEmployee()
emp1.displayCount()
