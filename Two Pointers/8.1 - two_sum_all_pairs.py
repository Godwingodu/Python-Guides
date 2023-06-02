# Two sum return all pairs
"""
k   => 7
i/p => [1,2,3,4,5,6,7]
o/p => [[1,6],[2,5],[3,4]] return all pair (reverse of pair and pair of same - not needed)
"""
limit = int(input())
array = [int(input()) for i in range(limit)]       # Array should be sorted
k_val = int(input())

def two_sum_all_pair(arr,size,k):
    left   = 0
    right  = size - 1
    result = []
    while left < right:
        if arr[left] + arr[right] < k:
            left += 1
        elif arr[left] + arr[right] > k:
            right -= 1
        else:
            result.append([arr[left],arr[right]])
            left  += 1
            right -= 1
        
    return result


print(two_sum_all_pair(array,limit,k_val))