# // try except
try:
   print(x)
except:
   print("An exception occurred")

print()

try:
   print(x)
except NameError:
   print("Variable x is not defined")
except:
   print("Something else went wrong")

print()

# Else
# The try block does not raise any errors, so the else block is executed:
# You can use the else keyword to define a block of code to be executed if no errors were raised:
try:
   print("Hello")
except:
   print("Something went wrong")
else:
   print("Nothing went wrong")
finally:
   print("Finally bloc")

print()

# Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
   print(x)
except:
   print("Something went wrong")
finally:
   print("The 'try except' is finished")

# Raise an exception
# To throw (or raise) an exception, use the raise keyword.
x = -1
if x < 0:
   raise Exception("Sorry, no numbers below zero")
