# Creating the dictionary

a = { "a":"alpha", "b":"beta", "c": "gamma"}              # a dictionary containing data in key value pair.

print(a)                                                  # printing the dictionary a .

# Creating a multidimensional dictioanry

b = {"a":[1,2,3], "b":{"a":"alpha", "b":"beta", "c": "gamma"}, "num": 2}   # A multidimensional dictionary consisting of nested list as well as dictionary


# Accessing th characters of the list

print(a["b"])                      # Accessing the elements corresponding to key "b".

print(b["b"]["a"])                 # Accessing and printing the elements of nested dictionary.

# dictionary method

# getting all the keys of our dictionary
# keys( ) method

print(a.keys())

print(b.keys())

# getting all the values of a dictionary
# values( ) methd

print(a.values())

print(b.values())

# getting all the key value pair of the dictionary
# items( ) method

print(a.items())

print(b.items())