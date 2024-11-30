# creating the two parent class

class parent_1:
    def function_1(self):
        return "I am parent_1"

class parent_2:
    def function_2(self):
        return "I am parent_2"



# Single Inhertiance

# creating a class inherting propery from a class

class child_1(parent_1):
    def fuction_3(self):
        return " I am  child 1"

# creating an object of child_1 class

obj_1 = child_1()

# calling the parent class function from the child class

print(obj_1.function_1())


# Multiple Inheritance

# Creating a child class inheriting properties from multiple classes

class child_2(parent_1,parent_2):
    def function_4(self):
        return "I am a child 2"

# creating a object of child_2 class

obj_2 = child_2()

# calling the two parent class functions

print(obj_2.function_1())
print(obj_2.function_2())

# Multilevel Inheritance

# creating a grand child class inherting the properties from child  class

class grand_child(child_1):
    def function_5(self):
        return "I am grand child"

# defining an object of grand_child class

obj_3 = grand_child()
# calling the parent class function from grand_child class object

print(obj_3.function_1())
print(obj_3.function_5())
print(obj_3.fuction_3())


# Hierarichal Inhertiance

# creating another class inheriting property from the parent class

class child_3(parent_1):
    def function_6(self):
        return " I also inherit from parent 1"

