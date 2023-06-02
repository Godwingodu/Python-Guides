# Two Sum With Duplicates and return all pairs | Input will contain duplicates but before pblm there was not duplicates | Array sorted as always
"""
k   => 10
i/p => [1,1,2,3,4,6,9,9]
o/p => [[1,9],[6,4]] return all pair (reverse of pair and pair of same - not needed)
"""
limit = int(input())
array = [int(input()) for i in range(limit)]                 # Array should be sorted
k_val = int(input())

def two_sum_all_pair(arr,size,k):
    left   = 0
    right  = size - 1
    result = []
    while left < right:
        if arr[left] + arr[right] < k:
            left  += 1
        elif arr[left] + arr[right] > k:
            right -= 1
        else:
            result.append([arr[left],arr[right]])
            left  += 1
            right -= 1

            while left < right and arr[left] == arr[left-1]:   # To skip duplicates | left
                left  += 1                                  
            while left < right and arr[right] == arr[right+1]: # To skip duplicates | right
                right -= 1
        
    return result


print(two_sum_all_pair(array,limit,k_val))