# Square Patterns

# Type 1
n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n, end='')
    print()

"""
4
4444
4444
4444
4444
"""

# Type 2
n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j, end='')
    print()

"""
4
1234
1234
1234
1234
"""

# Type 3
n = int(input())
for i in range(1,n+1):
    for j in range(n,0,-1):
        print(j, end='')
    print()

"""
4
4321
4321
4321
4321
"""

# Type 4
n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(ord('A') + j - 1 ), end='')
    print()

"""
4
ABCD
ABCD
ABCD
ABCD
"""

# Type 5
n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(ord('A') + j + i - 2 ), end='')
    print()

"""
4
ABCD
BCDE
CDEF
DEFG
"""