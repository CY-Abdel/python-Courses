# Python is an object oriented programming language.

class MyClass:
   x = 5


p1 = MyClass()
print(p1.x)


class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def __str__(self):
      return f"{self.name} is {self.age} years old"

   def myfunc(self):
      print("Hello my name is " + self.name)


p2 = Person("juba", 29)

p2.myfunc()
print(p2)
print()
"""
Note: The self parameter is a reference to the current instance of the class,
and is used to access variables that belong to the class.
   Use the words mysillyobject and abc instead of self:
   def __init__(mysillyobject, name, age)
"""
p2.age = 30
print(p2)
p2.myfunc()

# Delete Object Properties
del p2.age
print(p2.name)

# Delete Objects
del p2

