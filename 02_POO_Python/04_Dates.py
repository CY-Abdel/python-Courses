# Dates
import datetime
import locale

# Configurer la locale à 'fr_FR'
locale.setlocale(locale.LC_TIME, 'fr_FR')

x = datetime.datetime.now()
print(x)
print(x.date())
print(x.weekday(), end=" => ")
print(x.strftime("%A"))
print(x.day)
print(x.month)
print(x.year)

print()
# Creating Date Objects
x = datetime.datetime(2020, 5, 17)

print(x)
print()

# The strftime() Method
"""
   The datetime object has a method for formatting date objects into readable strings.
   The method is called strftime(), and takes one parameter, format,
   to specify the format of the returned string:
 """
import datetime

x = datetime.datetime.now()

print(x.strftime("%a"), end=" or ")
print(x.strftime("%A"))
print(x.strftime("%d"))
print(x.strftime("%b"), end=" or ")
print(x.strftime("%B"), end=" or ")
print(x.strftime("%m"))
print(x.strftime("%y"), end=" or ")
print(x.strftime("%Y"))

print()
# Afficher la date en français
print(x.strftime("%a %d %b %y"))
print(x.strftime("%A %d %B %Y"))

print()

# Formatage de la date avec différents séparateurs
date_format_slash = x.strftime("%a %d %b %Y").replace(' ', '/').replace('./', '/')
date_format_dash = x.strftime("%a %d %b %Y").replace(' ', '-').replace('.-', '-')
date_format_underscore = x.strftime("%a %d %b %Y").replace(' ', '_').replace('._', '_')

# Afficher les résultats
print("Avec /: =>", date_format_slash)
print("Avec -: =>", date_format_dash)
print("Avec _: =>", date_format_underscore)
