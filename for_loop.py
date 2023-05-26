""" 
for loop in python is achieved using a range function.
range(start,end,step) - generates a sequence of numbers starting from start, increments by step and stops before end.
by default start = 0 and step = 1 

"""
# list of numbers from 0 - 10
print(list(range(11)))

# list of numbers from 1 - 10
print(list(range(1,11)))

# list of even numbers in limit upto 10
print(list(range(2,11,2)))

# list of odd numbers in limit upto 10
print(list(range(1,11,2)))

# print numbers from 1 - 10
for i in range(1,11): 
    # start = 1 & end = (n+1) => 11 | i.e. 10+1 | so upto 10  
    print(i)

# print numbers from 1 - 10 in reverse
for i in range(10,0,-1): 
    # start = 10 & end = (n-1) => 0 | i.e. 1-1 | so upto 1
    print(i)



