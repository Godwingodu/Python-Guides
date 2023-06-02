# Sort an Array of 0s and 1s | Approach => 'Hoare's Partition'
"""
Hoere's Partition :-
- While Loop
- 2 pointers - left and right : left from start & right from end (traverse)
               here, left till find 1 & right till find 0 (traverse) | swap
"""
limit = int(input())
array = [int(input()) for i in range(limit)]

def sort_array_zero_one(arr,size):
    left = 0
    right = size - 1
    while left < right:
        while left < size - 1 and arr[left] == 0:
            left += 1
        while right >= 0 and arr[right] != 0:
            right -= 1
        
        if left < right:
            arr[left],arr[right] = arr[right],arr[left]
            left  += 1
            right -= 1
    
    print(arr)


sort_array_zero_one(array,limit)        
