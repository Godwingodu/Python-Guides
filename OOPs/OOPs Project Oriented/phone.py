from main import Item

# Inheritance
class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call super function to access to all attributes / methods in Parent Class
        super().__init__(name, price, quantity)

         # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero!"

        # Assign to self object
        self.broken_phones = broken_phones
    
    # Method overriding we override the repr method in base class so this will work now
    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity})"


phone1 = Phone("jscPhonev10", 500, 5, 1)
########################################
"""
Here, when we call Item.all we get [Phone('jscPhonev10', 500, 5)] coz, since we bypass constructor overriding and access constructor of base class
when we call Item.all that init method of base class will work and since we pass its param like "super().__init__(name, price, quantity)"
we will get those printed as o/p . But instead pf printing o/p as "[Item('jscPhonev10', 500, 5)]" its printed as "[Phone('jscPhonev10', 500, 5)]"
coz here we overrided the __repr__ method in base class and use that method with same name and defined it as above so, when a object is printed
from this class repr method in this class works instead of repr in base class (because we overided it otherwise not) .

"""
print(Item.all)                       # [Phone('jscPhonev10', 500, 5)]
# print(phone1.all)                   # [Phone('jscPhonev10', 500, 5)]
###########################################
