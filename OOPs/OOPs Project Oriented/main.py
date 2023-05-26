# OOPs Project using a Shop as Example 
import csv

class Item:
    pay_rate = 0.8                                                                 # The price after 20% discount
    all      = []                                                                  # Store all instances (products) created in shop

    def __init__(self, name: str, price: float, quantity=0):                       # Define argument type using :
        # Run validations to the received arguments use assert
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to variables to self or instance object
        self.__name = name
        self.price = price
        self.quantity = quantity

        # When 'obj is created' that instance will be appended to the class variable (all) thats why we put this in __init__
        Item.all.append(self)
    
    # Getters  [Used to make a attribute read-only, i.e if we set name for an obj at instantiation then we can't change it by (obj.name='newname') unless u use setters]
    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name
    
    # Setters [Used to make getters inactive or to overcome them] | To still change attribute name after obj creation (eventhough we used getters to prevent it)
    @name.setter
    # @name.setter = name => above getter fn name | syntax getter_fn_name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        return self.price * self.pay_rate                                          # Instead of accessing pay_rate from class level we can access it from intance level
                                                                                   # so that we specify our own % for specific product without changing orginal pay_rate . So one with specific % will use that and other with no specific % will use the orginal pay_rate .
    @classmethod
    def instantiate_from_csv(cls):
        # Setting csv file to open and read etc # defaults
        with open('C:\\Users\sahal\OneDrive\Desktop\Interview Preperation\Python Basics\OOPs\OOPs Project Oriented\data.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(                                                                 # Getting data from csv and passing as param to Class for creating objects 
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )
    
    # Check whether given number is integer or not
    @staticmethod
    def is_integer(num):                                                          # In staticmethod there is no req param like in classmethod like cls (class) etc. 
        # We will count out the floats that are point zero => i.e: 5.0, 10.0
        if isinstance(num, float):
            return num.is_integer()                                               # Count out the floats that are point zero => Return True if the float is an integer.
        elif isinstance(num, int):
            return True
        else:
            return False

    # Define what to print or display when the object is printed as whole. We can use __str__ if are not representing obj as whole i.e if using self.var_name etc 
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


# Instantiating objects by passing data directly [1]
""" 
 item1 = Item("Phone", 100, 1)
 item2 = Item("Laptop", 1000, 3)
 item3 = Item("Cable", 10, 5)
 item4 = Item("Mouse", 50, 5)
 item5 = Item("Keyboard", 75, 5 
"""
# Instantiating objects by passing data stored in a csv file [2]
"""
Item.instantiate_from_csv()
"""

# Printing all items
"""
print(Item.all)                                                                      # [Item('Phone', 100, 1), Item('Laptop', 1000, 3), Item('Cable', 10, 5), Item('Mouse', 50, 5), Item('Keyboard', 75, 5)] 
# Checking given number is integer
print(Item.is_integer(1.1))
"""



# print(item1.apply_discount())                                                      # 80.0 price
# item2.pay_rate = 0.7                                                               # If u want specific % for a product u can assign the % for pay_rate from the instance level than class level
# print(item2.apply_discount())                                                      # 700.0 price
