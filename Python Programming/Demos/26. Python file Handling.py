# creating a file in python

f = open("first_file.txt", "w")                      # using the w mode

# writing to the file

f.write("This is my first file")

# closing the file

f.close()

# opening the file for reading

f = open("first_file.txt", "r")                      # Using the r (read) mode

# reading the file

print(f.read())

# closing the file

f.close()

# Appending to the existing file

f =  open("first_file.txt", "a")                     # Using the a (append)  mode

# appeding to the file

f.write("This is my second line")

# Closing the file

f.close()

# reading the file again

f = open("first_file.txt","r")

# reading the file

print(f.read())