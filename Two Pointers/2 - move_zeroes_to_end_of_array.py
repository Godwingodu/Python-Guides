# Move all Zeroes to End Of Array | Approach => 'Lumutos Partition'
"""
[1,2,0,3,0,0] => [1,2,3,0,0,0]

Main Logic:-
        if arr[i] == 0:
            arr[i],arr[high] = arr[high],arr[i]  # swap
            high -= 1
"""
limit = int(input())
array = [int(input()) for i in range(limit)]

def zeros_to_end(arr,size):
    high = size - 1
    for i in range(size-1,-1,-1):
        if arr[i] == 0:
            arr[i],arr[high] = arr[high],arr[i]
            high -= 1
        
    print(arr)


zeros_to_end(array,limit)