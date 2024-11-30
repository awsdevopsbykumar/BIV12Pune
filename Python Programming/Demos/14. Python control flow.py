# Python control flow
# Boolean Expression

print(42 == 43)

print(43 == 43)


# control flow statement
# checking if a number is even or odd

num = 4

if num% 2 == 0:
    print("Even number")
else:
    print("Odd number")

num = 5

if num% 2 == 0:
    print("Even number")
else:
    print("Odd number")


# elif ladder

# Giving the Grade to student belonging to a class based on marks scored

marks = 75


if marks>90:
    print("A grade")
elif 90>marks>80:
    print("B grade")
elif 80>marks>70:
    print("C grade")
elif 70>marks>60:
    print("D grade")
else:
    print("Failed")


# nested if else:
# Problem statement : check a number is even or odd, if the no is even and less than 10 then program should give output "even and less than 10"
# if the no is even but greater than 10 then program should give the output "even and greater than 10"
# if the no is odd and  greater than 10 should give an output of "odd and greater than 10"
# if the no is odd and  less than 10  then program should give "odd and less than"


number = 25

if number%2 == 0:
    if number >= 10:
        print("Even and greater than 10")
    else:
        print("Even and less than 10")

else:
    if number >=10:
        print("Odd and greater than 10")
    else:
        print("Odd and less than 10")















