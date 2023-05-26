# Diamond Patterns
"""
This type of patterns are similar to isosceles triangle patterns and can be created from them.
[ isosceles + inverted isosceles with one row less (flip) => diamond pattern ]
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
        print('*', end='')
    for l in range(i-1,0,-1):
        print('*', end='')
    print()
for i in range(n-1,0,-1):  # n-1 coz its diamond upto 4 rows we will get from 1st i loop after that we want to get its flip thats in 3 2 1 order  
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
 *****
  ***
   *
"""