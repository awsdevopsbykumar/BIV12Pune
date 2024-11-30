
# creating a class item


class my_class:
    pass

# creating a class consisting different item

class item:                                                   # creating an item class 
    def __init__(self,  Name, Price, Quantity):                      # initialiser function                  
        self.name = Name                                      # creating the name attribute                           
        self.price = Price                                    # creating the name attribute  
        self.quantity = Quantity                              # creating the name attribute  

    def calculate_price(self):
        c = self.price * self.quantity
        #print(c)
        return c 


obj_1 = item("Phone", 100, 50)                                # creating an object of class item
obj_2 = item("Shoes", 50, 200)                                # creating an object of class item



print(obj_1.calculate_price())                                   # calling the calculate_price function from the object 1
print(obj_2.calculate_price())     

    



