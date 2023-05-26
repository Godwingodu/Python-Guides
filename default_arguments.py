"""
Default arguments are arguments we define as default it will work if
we dont pass any value for them at function call, then the default value 
set to them will be taken. But if we pass a value for them then the value 
passed by user will be taken instead of the default value

"""
def getSum(a,b,c=0):
    print(a+b+c)

getSum(1,2)                 # O/P => 3   |  value of c will be default:0
getSum(1,2,3)               # O/P => 6   |  value of c will be not default:0 as we pass value for it

def getSum(a,b=0,c=0):
    print(a+b+c)

getSum(1)                   # O/P => 1   |  value of b, c will be default:0

"""
Note:-
    def getSum(a=0,b,c=0):
    We can't give like this a non-default argument shall not be followed by a default-argument,
    so try to give default args after all non-default args .
"""

# Params are assigned to Args respectively
def printNum(a,b=2,c=3):
    print('a:',a)
    print('b:',b)
    print('c:',c)

printNum(1)                  # O/P => a: 1, b: 2, c: 3  
printNum(1,0,7)              # O/P => a: 1, b: 0, c: 7
printNum(c=10,b=5,a=0)       # O/P => a: 0, b: 5, c: 10

