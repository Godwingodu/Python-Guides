# Two sum | Return one pair
"""
k   => 7
i/p => [1,2,3,4,5,6,7]
o/p => [2,5] return any one pair
"""
limit = int(input())
array = [int(input()) for i in range(limit)]       # Array should be sorted
k_val = int(input())

def two_sum(arr,size,k):
    left  = 0
    right = size - 1
    while left < right:
        if arr[left] + arr[right] < k:
            left += 1
        elif arr[left] + arr[right] > k:
            right -= 1
        else:
            return [arr[left],arr[right]]
        
    return []                                      # If no pairs return empty array


print(two_sum(array,limit,k_val))