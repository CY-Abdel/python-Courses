# ***************** Python Functions
def my_function():
   print("Hello from a function")


my_function()


def my_function(name):
   print("Salut " + name)


my_function("juba")
my_function("az")
my_function("mel")


# Arbitrary Arguments, *args
def my_function(*kids):
   print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "juba")


# Keyword Arguments
def my_function(child3, child2, child1):
   print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="juba")


# Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
   print("His last name is " + kid["lname"])


my_function(fname="Abdel", lname="Juba")

print()


# Default Parameter Value
def my_function(country="Norway"):
   print("I am from " + country)


my_function("Sweden")
my_function()
my_function("Brazil")


# Passing a List as an Argument
def my_function(food):
   for x in food:
      print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Return Values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


# Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

# 1
# 3
# 6
# 10
# 15
# 21

"""Iteration 1 (k = 6) :

result = 6 + tri_recursion(5)
Appel récursif : tri_recursion(5)
Iteration 2 (k = 5) :

result = 5 + tri_recursion(4)
Appel récursif : tri_recursion(4)
Iteration 3 (k = 4) :

result = 4 + tri_recursion(3)
Appel récursif : tri_recursion(3)
Iteration 4 (k = 3) :

result = 3 + tri_recursion(2)
Appel récursif : tri_recursion(2)
Iteration 5 (k = 2) :

result = 2 + tri_recursion(1)
Appel récursif : tri_recursion(1)
Iteration 6 (k = 1) :

result = 1 + tri_recursion(0)
Appel récursif : tri_recursion(0)
Iteration 7 (k = 0) :

result = 0 (condition de base atteinte, la récursion s'arrête)
"""
