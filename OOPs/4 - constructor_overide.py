# Constructor Overriding
"""
Here, When we inherit BaseClass into SubClass and if both has construtor method in them then, Constructor of
SubClass will override the constructor of BaseClass as below example .
Note :- if SubClass dont have construtor then constructor of BaseClass will work
"""
class BaseClass:
    def __init__(self):
        print('Base Init')
    
class SubClass(BaseClass):
    def __init__(self):
        super().__init__()
        print('Sub Init')
    

obj1 = SubClass()                       # Sub Init

# Using Super() we can access methods in Base Class or Class we Inherit
"""
If we want access the constructor of BaseClass too in SubClass (bypass overriding),
We can use a method - super()
Then o/p of above example will be  =>  # Base Init  # Sub Init
""" 