# Multilevel Inheritance
# Refer Multiple Inheritance same logic here too
class First():
    def display(self):
        print('First')

class Second(First):
    def display(self):
        print('Second')

class Third(Second):
    def display_third(self):
        print('Third')


obj1 = Third()
obj1.display_third()
obj1.display()                      # Second
