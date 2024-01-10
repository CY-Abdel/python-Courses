# RegEx Module
# Import the re module:
import re

txt = "Random String"

# find all maj letters
x = re.findall(r"[A-Z]", txt)
print(x)

x = re.search("^Ra.*ing$", txt)
print(x.group())  # Random String
"""
^ : Il ancre le début de la chaîne, indiquant que la correspondance doit commencer dès le début de la chaîne.
Ra : C'est une séquence littérale signifiant que la chaîne doit commencer par les caractères "Ra".
.* : Cela signifie "n'importe quel caractère (excepté une nouvelle ligne) zéro ou plusieurs fois". En d'autres termes, cela permet de capturer n'importe quelle séquence de caractères entre "Ra" et "ing".
ing : C'est une séquence littérale signifiant que la chaîne doit se terminer par les caractères "ing".
$ : Il ancre la fin de la chaîne, indiquant que la correspondance doit se terminer à la fin de la chaîne.
"""

resultat = re.search(r"\bRandom\b", txt)
if resultat: print(resultat.group())

# Utilisation de la recherche pour trouver "dom Str"
resultat = re.search(r"dom Str", txt)
if resultat: print(resultat.group())

txt = "random string"
# Utilisation de la recherche pour trouver "R**om S*r"
x = re.findall("ran..m", txt)
print(x)

# ***************** The findall() Function
# The findall() function returns a list containing all matches.
txt = "The rain in Vde ai"
x = re.findall("ai", txt)
print(x)

print()
# The search() function searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned
txt = "The rain in Spain"
x = re.search(r"\s", txt)

print("The first white-space character is located in position:", x.start())

# ********************** The split() Function
txt = "The rain in Vde"
x = re.split(r"\s", txt)
print(x) # ['The', 'rain', 'in', 'Vde']

# specifying the maxsplit parameter
x = re.split(r"\s", txt, 1)
print(x) # ['The', 'rain in Vde']

print()

# The sub() Function
# The sub() function replaces the matches with the text of your choice
txt = "The rain in Vde"
x = re.sub(r"\s", "9", txt) #The9rain9in9Vde
print(x)
x = re.sub(r"\s", "9", txt, 2)
print(x)