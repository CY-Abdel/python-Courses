# ***************** Python while
i = 1
while i < 6:
   print(i)
   if i == 3:
      break
   i += 1

print()
i = 0
while i < 6:
   i += 1
   if i == 3:
      continue
   print(i)

print("\n*******for loop ***********")
# FOR LOOP
fruits = ["apple", "banana", "cherry"]
for x in fruits:
   if x == "banana":
      break
   print(x)

for x in range(2, 6):  # 2 inclu et 6 exclu
   print(x)

print()
# Increment the sequence with 3 (default is 1):
for x in range(2, 15, 3):
   print(x)

print()
for x in range(6):
   print(x)
else:
   print("Finally finished!")

adj = ["red", "big"]
fruits = ["apple", "cherry"]

for x in adj:
   for y in fruits:
      print(x, y)

print()

