# ***** les tuples *****

# A tuple is a collection which is ordered and unchangeable.
# ni ajouter ni supprimer ni modifier des éléments une fois le tuple créé

thistuple = ("banana", "apple", "cherry")
print(thistuple)

# ***** Tuples allow duplicate values:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# ***** Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))  # <class 'tuple'>

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))  # <class 'str'>

# A tuple can contain different data types
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
print(type(tuple1))
print()

thistuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(thistuple)
print(type(tuple1))
print()

# mon_tuple = (1, 2, 3)
# # Tentative de modification d'un élément, ce qui provoquera une erreur
# mon_tuple[0] = 4
#
# # Tentative d'ajout d'un élément, ce qui générera une erreur
# mon_tuple.append(4)
#
# # Tentative de suppression d'un élément, ce qui générera une erreur
# del mon_tuple[0]

# Access Tuple Items === idem que list

# Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

print()

# Update Tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) # ('apple', 'kiwi', 'cherry')

# add items in tulps with list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple) # ('apple', 'banana', 'cherry', 'orange')

# allowed to add tuples to tuples
thistuple = (1, 2, "cherry")
y = ("orange",)
thistuple += y

print(thistuple) # (1, 2, 'cherry', 'orange')

print()

# remove item
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple

#Unpacking tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green) #apple
print(yellow) #banana
print(red) #cherry

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green) # apple
print(yellow) #banana
print(red) # ['cherry', 'strawberry', 'raspberry']

print()

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

print()

# *********** Loop Tuples *********
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# Multiply Tuples => Join tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple) # ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

