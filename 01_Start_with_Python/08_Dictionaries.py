# ***************** Dictionaries
# Dictionaries are used to store data values in key:value pairs.
#
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
my_dict = {'a': 1, 'b': 2, 'c': 0, 'c': 0}
print(my_dict)

# get the value of the key
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 1964
}
print(thisdict)  # Duplicate values will overwrite existing values
print(thisdict["brand"])  # Ford
print(len(thisdict))  # 3

# The dict() Constructor
thisdict = dict(name="Juba", age=29, country="Japan")
print(thisdict)

# Accessing Items
x = thisdict["name"]
print(x)  # Juba
x = thisdict.get("name")
print(x)  # Juba

# Get Keys
# The keys() method will return a list of all the keys in the dictionary
x = thisdict.keys()
print(x)  # dict_keys(['name', 'age', 'country'])

print()

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x)  # before the change => dict_keys(['brand', 'model', 'year'])

car["color"] = "white"

print(x)  # after the change => dict_keys(['brand', 'model', 'year', 'color'])

# Get Values
x = thisdict.values()
print(x)  # dict_values(['Juba', 29, 'Japan'])

print()

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()

print(x)  # before the change => dict_values(['Ford', 'Mustang', 1964])

car["year"] = 2023

print(x)  # after the change => dict_values(['Ford', 'Mustang', 2023])

print()
x = car.values()

print(x)  # before the change => dict_values(['Ford', 'Mustang', 2023])

car["color"] = "red"

print(x)  # after the change => dict_values(['Ford', 'Mustang', 2023, 'red'])
print(type(x))  # <class 'dict_values'>

print()

# Get Items
x = thisdict.items()

print(x)  # dict_items([('name', 'Juba'), ('age', 29), ('country', 'Japan')])
print(type(x))  # <class 'dict_items'>

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()

print(x)  # before the change

car["color"] = "red"

print(x)  # after the change

print()

# Check if Key Exists
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Change Values
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018
thisdict.update({"model": "Flash"})

print(thisdict)  # {'brand': 'Ford', 'model': 'Flash', 'year': 2018}

# Add Dictionary Items
thisdict = {
    "brand": "Ford",
    "year": 1964
}

thisdict.update({"model": "Mustang"})
thisdict["color"] = "red"

print(thisdict)

print()

# Remove Dictionary Items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)  # {'brand': 'Ford', 'year': 1964}

# The popitem() method removes the last inserted item
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict)  # {'brand': 'Ford', 'model': 'Mustang'}

# The del keyword removes the item with the specified key name
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["brand"]
print(thisdict)  # {'model': 'Mustang', 'year': 1964}

# The clear() method empties the dictionary
thisdict.clear()
print(thisdict)  # {}

# The del keyword can also delete the dictionary completely
# print(thisdict)  # error : thisdict not defined

print("**************** loop **********")

# Loop Dictionaries
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(x, end=" => ")
    print(thisdict.get(x))
print()
for x in thisdict:
    print(x, end=" => ")
    print(thisdict[x])
print()
for x in thisdict.values():
    print(x)
print()
for x in thisdict.keys():
    print(x)
print()
for x, y in thisdict.items():
  print(x, "=>", y)
print()

# Copy Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
mydict = dict(thisdict)
print(mydict)

# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
print(myfamily["child2"]["name"])

print()
for x in myfamily:
    print(x)
for x in myfamily.values():
    print(x)
for x in myfamily.items():
    print(x)
