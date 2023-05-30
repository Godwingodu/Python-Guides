# Reversed Triangle Patterns
"""
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
        print('*', end='')
    print()

"""
4
   *
  **
 ***
****
"""

# Type 2
# n = int(input())
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(' ', end='')
#     for k in range(1,i+1):
#         print(k, end='')
#     print()

n = int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(' ', end='')
    for k in range(i):
        print(k+1, end='')
    print()

"""
4
   1
  12
 123
1234
"""