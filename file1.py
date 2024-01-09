if 5 > 2:
    print("Five is greater than two!")

x = 5
y = "Hello, World!"
print(x == y)
print(x)

# This is a comment
print("this is a >> #comment")

"""
This is a comment
written in
more than just one line
"""

# ******* Python Variables ************* #
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# str = string
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

# Get the Type
print(type(x)) # <class 'str'>
print(type(y)) # <class 'int'>

print("\"juba\" is the same as 'juba'")

a = 4
A = "Sally"
# A will not overwrite a
print("# A will not overwrite a")
print()

#   Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
print()

x = 5
y = "John"
print(x, y)

print()

# ** Global Variables **
x = "awesome"
def myfunc():
  print("Python is " + x)

myfunc()

print()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)  # Python is fantastic

myfunc()

print("Python is " + x) # Python is awesome

print()

# ** The global Keyword **
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

print()

#convert from int to float:
x = float(1) # 1.0

#convert from float to int:
y = int(2.8) # 2


print(x)
print(y)

print(type(x)) # <class 'float'>
print(type(y)) # <class 'int'>

print()
# ** Random Number **
import random
print(random.randrange(1,10))

print()

# ** Python Casting **
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x, y, z)

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
print(x, y, z)

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
print(x, y, type(z))


