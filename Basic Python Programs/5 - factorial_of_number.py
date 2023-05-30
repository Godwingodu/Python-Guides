# Factorial of a number
n = int(input())
fact = 1
for i in range(1,n+1):
    fact = fact*i

print(fact)
    
# Using recursive function
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = int(input())
print(factorial(num))