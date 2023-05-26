# if statement

n = 1
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2

print(n)

# use paranthesis for multiline conditions like and - or 
a, b = 1, 2
if ((a > 2 and a !=b) or a == b):
    a +=1 