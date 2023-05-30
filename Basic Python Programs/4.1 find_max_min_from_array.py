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