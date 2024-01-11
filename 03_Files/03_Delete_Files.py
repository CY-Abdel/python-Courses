# ********* Python File Delete

# **** must import the OS module, and run its os.remove() function
import os

# Check if File exist before remove:
if not os.path.exists("Assets/demofile3.txt"):
    f = open("Assets/demofile3.txt", "x")
    name = "demofile3.txt"
    print("the file '{}' was created".format(name))
    f.close()

f = open("Assets/demofile3.txt", "w")
f.write("\nthis text was added to the new file\n")
f.close()

f = open("Assets/demofile3.txt", "r")
print(f.read())
f.close()

# ** Check if File exist before remove:
if os.path.exists("Assets/demofile3.txt"):
    os.remove("Assets/demofile3.txt")
    print("The file was deleted")
else:
    print("The file does not exist")
