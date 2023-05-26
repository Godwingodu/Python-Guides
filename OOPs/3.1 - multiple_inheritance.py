# Multiple Inheritance
"""
In this, when inherited classes here, First & Second have a method with same name, so when we create a object for Third
and call this method here display() we will have a doubt which display will work (display of 1st or 2nd) ? => here, display of Second will work .
This is based on LefttoRight rule. When we call this display method it will check for this fn from left to right order in this case first it will
check it in Third -> Second -> First coz our Multiple Inheritance class -> [class Third(Second,First)]. If it was like [class Third(First,Second)]
it will check from Third -> First -> Second orderwise. If its found in any of these (in order wise) it will stop checking further at that moment itself .
"""
class First():
    def display(self):
        print('First')

class Second():
    def display(self):
        print('Second')

class Third(Second,First):
    def display_third(self):
        print('Third')


obj1 = Third()
obj1.display_third()
obj1.display()              # Second , coz when we check from LtoR this display will be first find in second() since display is not in Third()
                            # Once it found display in Second() it will stop searching and will not proceede to First() even if its there or not

