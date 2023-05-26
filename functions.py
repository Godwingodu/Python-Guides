# Functions in python 
""" 
syntax :
    def fun_name:
        block of code   
"""
# Funcion to print sum of numbers in a limit
def sum(limit):
    sum = 0
    for i in range(1,limit+1):
        sum += i 
    return sum
    
print(sum(3))          # O/P => 6

# Scope
"""
Scope of a variable is a region within which a variable is accessible .
Two Kinds- Local & Global variable

"""
a = 10                 # Global
def fun():
    b = 20             # Local
    print(b)

print(a)
fun()
# print(b)             'b' is not defined  |  coz b is local it is accessible only inside where it is defined i.e. fun()

# Accessing Local Varibale outside the function
def f():
    y = 20       
    return y

x = f()
print(x)                # By using return we can take that local y outside the function

# Global Keyword
i = 10                 # Global
def fn():          
    print(i)

print(i)               # O/P => 10
fn()                   # O/P => 10
""" i is global variable """

print('#################################')

c = 10                 # Global
def fnn():
    c = 20             
    print(c)

print(c)               # O/P => 10
fnn()                  # O/P => 20
"""
Here, when we print c we got 10, but when fnn is called it print c as 20,
as we saw at above ex. global var i is being considered while the fn print i when we call it,
but here the function considered the var c we declared inside the fnn as local not global and it uses it
instead of global c var. So to specify the fnn to use global c we use keyword global. If dont use it and 
give a var inside the function with same name as of a global var, then the function will not use the global var
it will use the local var declared inside the function instead .  ex. below --
"""

d = 10                 # Global
def fnnn():
    global d           
    print(d+10)

print(i)               # O/P => 10
fnnn()                 # O/P => 10
