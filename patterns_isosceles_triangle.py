# Isosceles Triangle Patterns
"""
This type of patterns are similar to reversed triangle patterns and can be created from them.

Revise:-
4
   *    1 => 4-1 spaces, 1 star
  **    2 => 4-2 spaces, 2 star
 ***    3 => 4-3 spaces, 3 star
****    4 => 4-4 spaces, 4 star

spaces = n - i
stars  = i 
"""

# Type 1
n = int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(' ', end='')
    for k in range(i):
        print(k+1, end='')
    for l in range(i-1,0,-1):
        print(l, end='')
    print()

"""
4
   1
  121
 12321
1234321
"""

# Type 2
# n = int(input())
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(' ', end='')
#     for k in range(i):
#         print(k+i, end='')
#     for l in range(i-1,0,-1):
#         print(l+k, end='')
#     print()

n = int(input())
for i in range(1,n+1):
    next_no = i
    for j in range(n-i):
        print(' ', end='')
    for k in range(i):
        print(next_no, end='')
        next_no += 1
    next_no -= 2
    for l in range(i-1,0,-1):
        print(next_no, end='')
        next_no -= 1
    print()

"""
4
   1
  232
 34543
4567654
"""

# Type 3
n = int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(' ', end='')
    for k in range(i):
        print('*', end='')
    for l in range(i-1,0,-1):
        print('*', end='')
    print()

"""
4
   *
  ***
 *****
*******
"""