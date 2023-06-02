# Move all Zeroes to Start Of Array | Approach => 'Lumutos Partition'
"""
[1,2,0,3,0,0] => [0,0,0,1,2,3]

Main Logic:-
        if arr[i] == 0:
            arr[i],arr[low] = arr[low],arr[i]  # swap
            low += 1
"""
limit = int(input())
array = [int(input()) for i in range(limit)]

def zeros_to_start(arr,size):
    low = 0
    for i in range(size):
        if arr[i] == 0:
            arr[i],arr[low] = arr[low],arr[i]
            low += 1
        
    print(arr)


zeros_to_start(array,limit)