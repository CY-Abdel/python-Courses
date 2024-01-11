# ********* Python File Write

# Write to an Existing File
"""
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file / creates the file if it does not exist

"w" - Write - will overwrite any existing content / creates the file if it does not exist
"""
f = open("Assets/demofile2.txt", "a")
f.write("\nNow the file has more content!")
f.close()

# ****** open and read the file after the appending:
f = open("Assets/demofile2.txt", "r")
print(f.read())
f.close()
print()

# ******** overwrite the content
f = open("Assets/demofile2.txt", "w")
f.write("Now the file overwrite any existing content!")
f.close()

f = open("Assets/demofile2.txt", "r")
print(f.read())
f.close()
print()
