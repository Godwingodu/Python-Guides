# Find maximum, minimum number in an array
def max_min(arr):
    max = arr[0]
    min = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]

        if arr[i] < min:
            min = arr[i]
        
    print("Largest Number is : ",max)
    print("Smallest Number is : ",min)


limit = int(input())
array = [int(input()) for i in range(limit)]

max_min(array)

################################################
list = [2,3,4,5,100,1000,0]
max = float('-inf')
min = float('inf')

for i in list:
    if i >= max:
        max = i
    
    if i <= min:
        min = i

print(min)
print(max)