# Python Lambda
x = lambda a: a + 10
print(x(5))

x = lambda a, b: a * b
print(x(5, 6))

x = lambda a, b, c: a + b + c
print(x(1, 2, 3))

def myfunc(n):
  return lambda a : a * n

print()

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) #22
print(mytripler(11)) #33
