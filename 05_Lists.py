# Python Lists
mylist = ["apple", "banana", "cherry"]
print(mylist)

# Allow Duplicates
mylist = ["apple", "banana", "cherry", "apple"]
print(mylist)
print(len(mylist))
print(type(mylist))

print()

# list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]
print(list1)

"""
# Python Collections (Arrays)
# There are four collection data types in the Python programming language:
#
    # List is a collection which is ordered and changeable. Allows duplicate members.
    # Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    # Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    # Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""
print()
mylist = ["apple", "banana", "cherry"]

# Access Items
print(mylist[0])

# Print the last item of the list
print(mylist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
if "tutu" not in thislist:
    print("no")
else:
    print("Yes, 'titi' is in the fruits list")
print()

# Change List Items
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) # ['apple', 'watermelon']

# add an item to the end of the list, use the append() method
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) # ['apple', 'banana', 'cherry', 'orange']

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) # ['apple', 'orange', 'banana', 'cherry']

# Remove the first occurance
thislist.remove("banana")
print(thislist)

# ** Remove Specified Indexy
# The pop() method removes the specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Remove the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist
# print(thislist) => # NameError: name 'thislist' is not defined

# The clear() method empties the list.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Loop Lists
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

print()

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

print()

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist) # ['apple', 'banana', 'mango']

newlist = [x for x in fruits if x != "apple"]
print(newlist) # ['banana', 'cherry', 'kiwi', 'mango']

newlist = [x for x in range(10)]
print(newlist) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

newlist = [x for x in range(10) if x < 5]
print(newlist) # [0, 1, 2, 3, 4]

newlist = [x.upper() for x in fruits]
print(newlist) # ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

newlist = ['vde' for x in fruits]
print(newlist) # ['vde', 'vde', 'vde', 'vde', 'vde']

print()

print(fruits)
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist) # ['vde', 'vde', 'vde', 'vde', 'vde']

# Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

# Sort the list numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) # [23, 50, 65, 82, 100]

# Sort the list descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist) # ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist) # [100, 82, 65, 50, 23]

# Sort by distance to 50
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist) # [50, 65, 23, 82, 100]

print()

# probleme with : Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)# ['Kiwi', 'Orange', 'banana', 'cherry']

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key= str.lower)
print(thislist)
thislist.sort(key= str.upper)
print(thislist) # ['banana', 'cherry', 'Kiwi', 'Orange']

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) # ['cherry', 'Kiwi', 'Orange', 'banana']

print()

# *** Copy a List ***
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Join Two Lists
    # avec : + // loop for // extend
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# // ---- //

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)
print(list1)

# **********
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3, 1, 2, 2]

list1.extend(list2)
print(list1)
print(list1.count("a")) # 1 occurence
print(list1.count(2)) # 3 occurences

