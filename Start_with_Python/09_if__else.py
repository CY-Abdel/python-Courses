# ***************** Python If ... Else
a = 33
b = 200
if b > a:
    print("b is greater than a")

b = 33
if b > a:
    print("b is greater than")
elif b == a:
    print("b is equal")

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("A is greater than B")

# Short Hand If
if a > b: print("a is greater than b")

# Short Hand If ... Else
a = 2
b = 330
print('A') if a > b else print('B')

# One line if else statement, with 3 conditions
a = 330
b = 330
print("A") if a > b else print("a=b") if a == b else print("B")

print()

#The and keyword is a logical operator,
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# The or keyword
if a > b or a > c:
  print("At least one of the conditions is True")

# Test if a is NOT greater than b
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
print()

# Nested If
# if statements inside if statements, this is called nested if statements
x = 41
if x > 10:
  print("Above ten,")
  if x > 50:
    print("and also above 50!")
  else:
    print("but not above 50.")