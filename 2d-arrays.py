# 2D-List 

li = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

# Length
print(len(li))          # O/P => 3  |  Length of list 
print(len(li[0]))       # O/P => 3  |  Length of list at index 0

# Accessing elements
print(li[0][0])         # O/P => 1  |  1st zero gives list at index 0 (list[1,2,3]), 2nd zero gives Element at 0 index of this list 
print(li[2][2])         # O/P => 9  

# Jagged List (2D-List with uneven numbers or size)
jl = [
        [1,2,3],
        [4,5],
        [6]
    ]

# Length
print(len(jl))          # O/P => 3  |  Length of list 
print(len(jl[1]))       # O/P => 2  |  Length of list at index 0

# Accessing elements
print(jl[0][0])         # O/P => 1  
print(jl[2][0])         # O/P => 6

# Iterate through 2D-List and print each element in different line
for i in range(len(li)):
    for j in range(len(li)):
        print('#',li[i][j]) 

"""
O/P    
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

"""
# Iterate through Jagged List and print each element in different line
for i in range(len(jl)):
    for j in range(len(jl[i])):
        print('$',jl[i][j]) 

"""
O/P    
$ 1
$ 2
$ 3
$ 4
$ 5
$ 6

"""
