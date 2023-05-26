# Method Overriding
"""
Here, When we inherit BaseClass into SubClass and if both has a method with same name in them then,
method of SubClass will override the method of BaseClass as below example .
Note :- if SubClass dont have method with same name then method of BaseClass will work .
Similar to constructor overriding .
"""
class BaseClass:
    def set_name(self,name):
        self.name = name
        print('set name from base class')
    
class SubClass(BaseClass):
    def set_name(self,name):
        super().set_name('rishal')
        self.name = name
        print('set name from sub class')


obj1 = SubClass()                     
obj1.set_name('Sahal')                           # Set name from sub class

# Using Super() we can access methods in Base Class or Class we Inherit
"""
If we want access the method with same name of BaseClass too in SubClass (bypass overriding),
We can use a method - super()
Then o/p of above example will be  =>  # Set name from base class  # Set name from sub class
""" 
