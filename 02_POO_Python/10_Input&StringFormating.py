# *** User Inputs & string formatting
"""
    Python 3.6 uses the *** input() method.
    Python 2.7 uses the *** raw_input() method.
"""
# username = input("Enter username:")
# print("Username is: " + username)

# String Formatting
"""
The format() method allows you to format selected parts of a string.
Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?

To control such values, 
add placeholders (curly brackets {}) in the text, 
and run the values through the format() method
"""
# txt = "je m'appelle {}"
# print(txt.format(username))
# print()

price = 49
txt = "The price is {} dollars"
print(txt.format(price)) # The price is 49 dollars

txt = "The price is {:.3f} dollars"
print(txt.format(price)) #The price is 49.000 dollars

# ************** Multiple Values **********
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price)) #I want 3 pieces of item number 567 for 49.00 dollars
print(myorder.format(itemno, price, quantity)) #I want 567 pieces of item number 49 for 3.00 dollars.

# *********** Index Numbers
"""# You can use index numbers (a number inside the curly brackets {0}) 
to be sure the values are placed in the correct placeholders"""
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price)) #I want 3 pieces of item number 567 for 49.00 dollars.

print()

age = 29
name = "Juba"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# ********* Named Indexes
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

