# Parse JSON - Convert from JSON to Python
"""
If you have a JSON string, you can parse it by using the json.loads() method.

The result will be a Python dictionary.
"""
import json
from pathlib import Path

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
print(type(x))

# parse x:
y = json.loads(x)
print(type(y))  # <class 'dict'>

# the result is a Python dictionary:
print(y["age"])

# JSON from path
data_json = Path('assets/data.json').resolve()

# Chargez les données depuis le fichier JSON
with open(data_json, 'r') as fichier:
   datas = json.load(fichier)

# Imprimez la valeur de la clé "age" pour chaque élément
print(datas)


# Convert from Python to JSON

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)



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

# convert into JSON:
y = json.dumps(myfamily)

# the result is a JSON string:
print(y)

print()
# Convert a Python object containing all the legal data types
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
print(json.dumps(x, indent=3))
print(json.dumps(x, indent=3, sort_keys=True))
