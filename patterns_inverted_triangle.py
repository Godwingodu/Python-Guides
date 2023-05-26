# Inverted Triangle Patterns

# Type 1
# n = int(input())
# for i in range(n+1,0,-1):
#     for j in range(1,i):
#         print('*', end='')
#     print()

n = int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print('*', end='')
    print()

"""
4
****
***
**
*
"""

# Type 2
n = int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i, end='')
    print()

"""
4
4444
333
22
1
"""
