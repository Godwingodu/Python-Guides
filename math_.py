# Normal Division
# With decimal
print(5 / 2)

# Floor Division
# Without decimal
print(5 // 2)

"""
Most languages round towards 0 by default but in python dividing (-3 // 2) gives unexpected results to fix this and for rounding towrads 0 
like other languages use normal division and convert it into int .

"""
print(-3 // 2) 
# -2 | unexpected o/p
print(int(-3 / 2)) 
# -1 | correct o/p

# Modulos Operator
print(10 % 3)
# o/p - 1

"""
Modding for negative values gives wrong results to fix this use fmod from math module

"""
print(-10 % 3) 
# o/p - 2 | not correct

# use this instead
import math
print(math.fmod(-10 , 3))
# o/p - -1

# Some more math helpers
print(math.floor(10 / 3))
print(math.ceil(10 / 3))
print(math.sqrt(2))
print(math.pow(10 , 3))



