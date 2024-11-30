# creating a function

# takes a number n amd multiply it by 5

def five_multiple(n):
    return 5*n

print(five_multiple(7))            # Calling the function

# using loops in function


def loop_use(i):
    for a in range(1,i+1):
        print(i)

loop_use(9)                # calling the fumction

# using the arbitrary argument:


def n_sum(*num):
    total = 0
    for i in num:
        total = total + i
    return total

print(n_sum(1,2,3,4))         # calling the function



# using the keyword argument

def keyword_function(**key_words):
    for i in key_words:
        print(key_words[i])


print(keyword_function( a ="alpha", b = "beta"))
