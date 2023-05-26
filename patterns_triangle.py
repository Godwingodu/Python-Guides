# Patterns helps us to understand looping concepts
# Pattern problems takes input from user and print some pattern in display
# Example
"""
4               5
*               *   
**              **
***             ***
****            ****
                *****           
"""
# How to solve?
"""
No.of rows = i (input = no.of rows)
No.of cols = j
What to print (some times different characters then we represent it in terms of n)
"""

# Triangle Patterns

# Type - 1
n = int(input())
for i in range(n):
    for j in range(i+1):
        print("*", end='')
    print()

"""
5
*
**
***
****
*****
"""

# Type - 2
n = int(input())
for i in range(n):
    for j in range(i+1):
        print(j+1, end='')
    print()

"""
5
1
12
123
1234
12345
"""

# Type - 3
n = int(input())
for i in range(n):
    for j in range(i+1,0,-1):
        print(j, end='')
    print()

"""
4
1
21
321
4321
"""

# Type - 4
n = int(input())
for i in range(1,n+1):         
    for j in range(1,i+1):
        print(j+i-1, end='')
    print()

"""
4
1
23
345
4567
"""

# Type - 5
n = int(input())
next_no = 1
for i in range(1,n+1):         
    for j in range(1,i+1):
        print(next_no, end='')
        next_no += 1
    print()

"""
4
1
23
456
78910
"""

