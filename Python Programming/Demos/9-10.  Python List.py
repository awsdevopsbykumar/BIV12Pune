# list creation

a = [1,2,3,4, "a","b","c","d"," John", 123]                    # variable "a" has a list which has a sequence of different data types namely numeric and string

# Nested list

b = [["a","b","c"],1,2,3,["alpha","beta","gamma"]]             # list contating the list  or nested list format


# Accessing the elements of the list

print(a[0])                         # Accessing and printing the first element of our list.

print(b[-1])                        # Accesssing and printing the last element of our list .

# Accessing the element of the nested list

print(b[0][2])                            # Accessing and printing the third character of the list stored as the first element of the main list.

# Slicing operation on the list

print(a[0:3])                             # Accessing and printing the element from zeroth to 2nd index.

#Python Methods

# append( ) method

a.append("new element")            # Adding the new element to the end of list a.

print(a)                           # Printing the list a.

#pop( ) method

a.pop( )                           # removing the last element of the list.

print(a)                           # printing the list.

a.pop(0)                           # removing the element at the zeroth index.

print(a)                           # printing the list.


# insert( ) method

a.insert(0,1)                      # inserting the element 1 at the zeroth index of the list "a"

print(a)

# remove( ) method

a.remove(4)                        # removing the element 4 from the list "a"

print(a)

# reverse( ) method

a.reverse()                        # reversing the list a

print(a)                           # printing the list a