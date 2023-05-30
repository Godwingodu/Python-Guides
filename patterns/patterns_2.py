"""
Printing Alphabet Patterns
ord('A')            => Gives Ascii of A
ord('A') + 3        => Gives Ascii of D
chr(ord('A'))       => Gives Character A
chr(ord('A') + 3)   => Gives Character D
"""

# Type - 6
n = int(input())
for i in range(1,n+1):         
    for j in range(1,i+1):
        print(chr(ord('A') + j - 1), end='')
    print()

"""
4
A
AB
ABC
ABCD
"""

# Type - 7
# n = int(input())
# for i in range(n):         
#     for j in range(i+1):
#         print(chr(ord('A')+j+i), end='')
#     print()

n = int(input())
for i in range(1,n+1):         
    for j in range(1,i+1):
        print(chr(ord('A') + j + i - 2), end='')
    print()

"""
4
A
BC
CDE
DEFG
"""

# Type - 8
n = int(input())
for i in range(1,n+1):         
    for j in range(1,i+1):
        print(chr(ord('A') + n-1 + j-1), end='')
    print()

"""
4
D
DE
DEF
DEFG
"""

# Type - 9
n = int(input())
for i in range(1,n+1):         
    for j in range(1,i+1):
        print(chr(ord('A') + n-1 + j-i), end='')
    print()

"""
4
4
D
CD
BCD
ABCD
"""