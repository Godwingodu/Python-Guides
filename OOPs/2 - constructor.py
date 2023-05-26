"""
Constructor in python is __init__ method, this method is called when a object is created .
It allots m/y for objects when its created. 2 types - default constructor (no param) & parameterized constructor .
By default its empty but whatever we give inside it will executed when object is created, for eg:- if we put a print
statement inside the __init__ it will be printed when the object is created.
Parametrized constructor is used when we want to pass some defaults or values while object is created or else default const. is used .
"""

class Student:

    year = 2023                         # Class variable its global to all methods inside this class, can be accessed inside all methods in this class

    def __init__(self,name,age,place):  # Constructor
        self.name  = name               # Instance variable | object inte ulile variable so vere objectne badikila oro obj kum ad different ai kidakum
        self.age   = age
        self.place = place
    
    def add_age(self):                  # Class method
        self.age   += 1

    def relocate(self,place):
        self.place = place  

    def display(self):
        print('Year : ', Student.year)
        print('Name : ', self.name)
        print('Age : ', self.age)
        print('Place : ', self.place)
    
    @classmethod                       # Using this method we can alter class variable year by calling the obj itself
    def add_year(cls):
        cls.year += 1
    
    @staticmethod                      # This is used when we want print or do something, as that will not affect the objects in class
    def display_welcome():
        print('Welcome')


obj1 = Student('Sahal',21,'Thrissur')
obj2 = Student('Rishal',17,'Calicut')

obj1.display()                         # Year :  2023, Name :  Sahal,  Age :  21, Place :  Thrissur
obj2.display()                         # Year :  2023, Name :  Rishal, Age :  17, Place :  Calicut

# If we decide to chnage place and increase age
obj1.add_age()
obj1.relocate('Kochi')
obj1.display()                         # Year :  2023, Name :  Sahal, Age :  22, Place :  Kochi [ age and place changed]

# To alter class variable [ Normal Approach ]
Student.year += 1                      # Unlike instance var, changing class var will affect all over the class since its not stored inside a particular instance and all coz, its global
obj1.display()                         # Year :  2024, Name :  Sahal, Age :  22, Place :  Kochi 

# To alter class variable [ Using @classmethod Approach ]
obj2.add_year()                        # Since year is global its value will be 2024 look above case, so now 2024+1=2025
obj2.display()                         # Year :  2025, Name :  Rishal, Age :  17, Place :  Calicut

# Calling Static Method
Student.display_welcome()              # Welcome
obj1.display_welcome()                 # Welcome