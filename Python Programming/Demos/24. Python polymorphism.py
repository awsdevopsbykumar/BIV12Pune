# Polymorphism with inheritane

# creating a parent class

class parent:
    def function_1(self):
        return " I am Parent"

# creating a child class inheriting the properties from the parent class and having the same function_2 but with the different definition

class child(parent):
    def function_1(child):
        return " I am a child"

# creating an object of the parent and child class and then calling the function_1

obj_1 = parent()
obj_2 = child()

print(obj_1.function_1())
print(obj_2.function_1())

# Polymorphism with classes


# Creating another class wtith the same function_1 but different definition.

class parent_2:
    def function_1(self):
        return " I have another definition"

# creating and calling an object of this parent_2 class

obj_3 = parent_2()

print(obj_3.function_1())



















