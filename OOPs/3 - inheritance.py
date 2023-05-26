# Inheritance
class BaseClass:
    def set_name(self, name):
        self.name = name

class SubClass(BaseClass):                 # Inheriting BaseClass
    def welcome(self):
        print('Welcome')
        
    def display_name(self):
        print(self.name)


obj1 = BaseClass()
# obj1.set_name('Sahal')

obj2 = SubClass()                         
obj2.set_name('Rishal')                    # As we inherited BaseClass we can access its method set_name() in the obj of SubClass like this  
obj2.display_name()
obj2.welcome()