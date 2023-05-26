# Tuples are similar to array but are immutable
tup = (1,2,3)               # OR  => tup = 1,2,3
print(tup[0])               # O/P => 1
print(tup[-1])              # O/P => 3

# Can't Modify
# tup[0] = 1

# Unpacking
a, b = (1,2)
print(a, b)                 # O/P => 1 2

# Single element tuple
c = (1,)

# Can be use as key for Hash Map/Set
# List can't be use as key for Hash Map/Set - unhashable type: 'list'
myMap = { (1,2):3 }
print(myMap[(1,2)])         # O/P => 3

mySet = set()
mySet.add((1,2))
print(mySet)                # O/P => {(1, 2)}

# Slicing similar to list

# List to tuple
print(tuple([1,2]))         # O/P => (1, 2)

# Min & Max
min(tup)
max(tup)

# Args in function
def fun(a,b,*args):
    print('a =', a)
    print('b =', b)
    print('args =', args)

fun(1,2,3,4,5,6)

"""
a = 1
b = 2
args = (3, 4, 5, 6)
When fn has 2 param and more than 2 arguments are given at function call,
then the 1st 2 arguments will store in respective params and the rest of
the args will be stored in the args as a tuple as shown above .
"""

