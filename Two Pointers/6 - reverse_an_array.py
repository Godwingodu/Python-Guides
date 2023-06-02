# By Traversing from both ends
limit = int(input())
array = [int(input()) for i in range(limit)]

def reverse_array(arr,size):
    left  = 0
    right = size - 1
    while left < right:
        arr[right],arr[left] = arr[left],arr[right]
        left  += 1
        right -= 1
    
    print(arr)


reverse_array(array,limit)