# python loops


# while loop

# printing and raising the number until the no becomes equal to 10 starting from 0

number = 0

while number!= 10:
    print(number)
    number  = number +1

# for loop

# using the for loop to generate a sequence:

# printing the sequence of numbers form 1 to 10

for i in range(0,10):
    print(i)


# performing operation with reference of different item of a sequence


for i in range(0,10):
    print(f"I am {i}")


# loop control statements

# break

a = [1,2,3,4,"find_me",5,6,7]

for i in a:
    if i == "find_me":
        print("I found you")
        break
    else:
        print(f"I found {i}")

# continue:

b = [1,2,3,4,"go pass me",5,6,7]

for i in b:
    if i == "go pass me":
        print("i will skip this")
        continue
    else:
        print(f"I found {i}")


# pass

c = [1,2,3,4,"I am pass", 5, 6, 7]


for i in c:
    if i == "I am pass":
        print(" you are pass")
        pass
    else:
        print(f"I found{i}")