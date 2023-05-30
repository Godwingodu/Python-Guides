# Largest among 3 numbers
def larget(num1,num2,num3):
    if (num1 >= num2) and (num1 >= num3):
        largest = num1

    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
        
    else:
        largest = num3
    
    return f"Largest number is {largest}"


a = int(input())
b = int(input())
c = int(input())

print(larget(a,b,c))
