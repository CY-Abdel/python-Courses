# Python Inheritance

class Person:
   def __init__(self, fname, lname):
      self.firstname = fname
      self.lastname = lname

   def printname(self):
      print(self.firstname, self.lastname)


# Use the Person class to create an object, and then execute the printname method:

x = Person("Juba", "Abdel")
x.printname()


class Man(Person):
   pass


# Now the Man class has the same properties and methods as the Person class
x = Man("Juba2", "Abdel2")
x.printname()

print()


class Student2(Person):
   def __init__(self, fname, lname):
      Person.__init__(self, fname, lname)


x = Student2("J3", "A3")
x.printname()


# Use the super() Function
# Python also has a super() function
# that will make the child class inherit all the methods and properties from its parent:
class Student3(Person):
   def __init__(self, fname, lname):
      super().__init__(fname, lname)


x = Student3("J4", "A4")
x.printname()


# Add Properties
class Student4(Person):
   def __init__(self, fname, lname):
      super().__init__(fname, lname)
      self.graduationyear = 2023


x = Student4("J5", "A5")
x.printname()
print(x.graduationyear)

print()


class Student5(Person):
   def __init__(self, fname, lname, year):
      super().__init__(fname, lname)
      self.graduationyear = year

   # Add Methods
   def welcome(self):
      print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


x = Student5("J6", "A6", 2023)
x.printname()
print(x.graduationyear)
x.welcome()
