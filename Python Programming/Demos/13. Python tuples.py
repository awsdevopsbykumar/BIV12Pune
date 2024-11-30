# creating the tuple

tuple_1 = (1,2,3,4)         # creating the tuple

print(tuple_1)              # printing the tuple "a"

# accessing the tuple

tuple_1[0]                 # accessing the first characters of our tuple

# Tuple Packing

tuple_2 = 1,2,3,4,5         # defining the tuple without parentheses

print(tuple_2)

# tuple Unpacking

(a,b,c,d) = tuple_1      # assigning the elements of tuple to the tuple of a variable

print(a)                  # printing the value stored in variable a

print(b)                  # printing the value stored in variable b

# tuple concatenation

tuple_3 = tuple_1 + tuple_2                 # adding the two tuples

print(tuple_3)

# tuple methods

# getting the first appearance of the element of the tuple

# index( ) method

print(tuple_1.index(2))

# getting the no of times item gor repeated in our tuple

# count( ) method

print(tuple_3.count(3))

