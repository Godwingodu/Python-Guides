# Operator Overloading
"""
In Python, we can change the way operators work for user-defined types.
For example, the + operator will perform arithmetic addition on two numbers, merge two lists, or concatenate two strings.
It is achievable because ‘+’ operator is overloaded by int class and str class. You might have noticed that the same built-in 
operator or function shows different behavior for objects of different classes, this feature in Python that allows the same operator
to have different meaning according to the context is called operator overloading.

"""
# + Operator Overloading in Python
"""
To overload the + operator, we will need to implement __add__() function in the class.
Class functions that begin with double underscore __ are called special functions in Python.
The special functions are defined by the Python interpreter and used to implement certain features or behaviors.
"""
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self):          # Special fn that returns a string representation of the object
        return f'X-Coordinate:- {self.x}, Y-Coordinate:- {self.y}'
        # return "({0},{1})".format(self.x, self.y)
    
    def __add__(self,other):    # Special fn that adds two objects
        x = self.x + other.x
        y = self.y + other.y
        return (x,y)


obj1 = Point(1,2)
obj2 = Point(3,4)

print(obj1)                     # X-Coordinate:- 1, Y-Coordinate:- 2
print(obj1 + obj2)              # (4, 6)

"""
In above ex, if we normally add obj1 + obj2, we will get error we can't add objects using +. But to make this possible we can use
some special fn's (dender methods) in python, and acheive this using operator overloading i.e we can overlaod + operator to add 2
objects (this feature in Python that allows same operator to have different meaning according to the context is called operator overloading.)

So, to add 2 objects we have a speical fn __add__ this helps to add 2 objects as given in above example . In the example __add__(self,other) here,
    self => 1st (obj1) argument, other => 2nd (obj2) argument .
    to get the str representation of objects we can use special fn __str__ . 
    there are also many other dender methods like __len__ etc .
"""