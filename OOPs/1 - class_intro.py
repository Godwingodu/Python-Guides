"""
Class is a blueprint or base model from which objects are created, these objects have different methods, features etc
Eg:- Soap Mould - Class | Soap - Object
"""
# Defining a Class
class MyClass():
    def get_name(self, name):      # self will have the obj as argument
        self.name = name           # creating variable | selfil ula objectinte ullil ayirikum ee value varuka or store aka
    
    def print_name(self):
        print('Hello',self.name)


# Creating Object from Above Class
obj1 = MyClass()                   # MyClass.get_name(obj)  |  this is happening when a object is created here obj is passed as param to the argument self of method()
obj2 = MyClass()

name = 'Sahal'
obj1.get_name(name)                 # Set name to the variable self.name for this object (obj1)
obj1.print_name()                   # Hello Sahal

obj2.get_name('Python')             # Set name to the variable self.name for this object (obj2)
obj2.print_name()                   # Hello Python