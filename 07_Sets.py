# ***************** Set
# Sets are used to store multiple items in a single variable.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

# Once a set is created, you cannot change its items, but you can remove items and add new items.
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Unordered
# Unordered means that the items in a set do not have a defined order.
# cannot be referred to by index or key

# Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) #{'apple', 'banana', 'cherry'}

# False and 0 is considered the same value
thisset = {"apple", "banana", 0, False, True}
print(thisset) # {'banana', 'apple', 0, True}

# Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset)) # 3

# The set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

print()

# Access Set Items
for x in thisset:
  print(x)

# Change Items
# Once a set is created, you cannot change its items, but you can add new items.

# Add Items
# To add one item to a set use the add() method.
thisset = {"apple", "banana", "cherry"}
thisset.add("sarra")
print(thisset)

# add items from another set into the current set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) # {'apple', 'pineapple', 'papaya', 'banana', 'cherry', 'mango'}

# The object in the update() method does not have to be a set,
# it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset) #{'orange', 'banana', 'kiwi', 'cherry', 'apple'}

# Remove Item => use the remove(), or the discard() method.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("cherry")
print(thisset)

# Remove a random item by using the pop() method
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# The clear() method empties the sets
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) # set()

print()

# The del keyword will delete the set completely
thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset) #this will raise an error because the set no longer exists

# Loop Sets
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# Keep ONLY the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

# Return a set that contains the items that exist in both set x, and set y
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

# Keep All, But NOT the Duplicates
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)  # {'google', 'banana', 'microsoft', 'cherry'}

# The symmetric_difference() method will return a new set,
# that contains only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

# The values True and 1 are considered the same value in sets,
# The values False and 0 are considered the same value in sets,
# and are treated as duplicates:
x = {"apple", "banana", "cherry", True, False}
y = {"google", 1, "apple", 2, 0}
z = x.symmetric_difference(y)
print(z) # {2, 'banana', 'google', 'cherry'}

