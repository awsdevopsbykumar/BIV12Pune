# Encapsulation
# creating a class with public, private and private memebers

class my_class:
    def __init__(self, name, age, school):
        self.name = name                       # public member
        self._age = age                        # protected member
        self.__school = school                 # private member


    def access_pvt_member(self):
        return self.__school


# creating an object of my_class

obj_1 = my_class("John",17,"ABC School")

# accessing the public attribute

print(obj_1.name)

# accessing the private member


#print(obj_1.__school)          # This should give the error

# accessing the private member

# name mangling method

print(obj_1._my_class__school)









