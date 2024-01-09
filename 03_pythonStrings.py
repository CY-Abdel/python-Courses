# Assign String to a Variable
a = "Hello"
print(a)

# ** Multiline Strings **
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

print (" *********** ")
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

print (" *********** ")

# ** Strings are Arrays **
a = "Hello, World!"
print(a[1])
print(a[0])
print(a[2])

print (" *********** ")
# ** Looping Through a String **

for x in "name":
  print(x)

print()  
a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)
print("vde" in txt)

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
  
print()

# Python - Slicing Strings
b = "Hello, World!"
print(b[2:5])

# Slice From the Start
b = "Hello, World!"
print(b[:4])

# Slice To the End
b = "Hello, World!"
print(b[3:])

print()
# Upper Case
a = "Hello, World!"
print("a.upper() => " , a.upper())

# Lower Case
a = "Hello, World!"
print("a.lower() => " , a.lower())

# Remove Whitespace in the start and the end
a = " Hello,   World! "
print(a.strip()) # returns "Hello, World!"

# Replace String
a = "Hello, juba!"
print(a.replace("H", "J"))

# split
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# String Concatenation
a = "Hello"
b = "vde"
c = a + " " + b
print(c)
print()

# String Format
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
""" I want 3 pieces of item 567 for 49.95 dollars. """

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
""" I want to pay 49.95 dollars for 3 pieces of item 567. """