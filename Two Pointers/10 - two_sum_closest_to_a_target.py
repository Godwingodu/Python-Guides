# Two Sum Closest to Target | Return any one pair
"""
k   => 5            |  k    => 4             |  k    => 5
i/p => [1,7,4,-3]   |  i/p  => [-1,2,1,-4]   |  i/p  => [-2,1,3,8]
o/p => [1,4]        |  o/p  => [2,1]         |  o/p  => [1,3] or [-2,8]
         5                       3                        4         6
"""
limit = int(input())
array = [int(input()) for i in range(limit)]   # Array should be sorted | no dupes | if not sorted sort it
k_val = int(input())

def two_sum_close_to_target(arr,size,k):
    if len(arr) < 2:
        return [-1,-1]
    
    arr.sort()

    left  = 0
    right = size - 1
    min_diff = float('inf')
    while left < right:
        sum  = arr[left] + arr[right]
        diff = k - sum
        if abs(diff) < abs(min_diff):
            min_diff = diff
            first    = arr[left]
            second   = arr[right] 
        
        if sum < k:
            left  += 1
        elif sum > k:
            right -= 1
        else:
            break
    
    return [first,second]
  

print(two_sum_close_to_target(array,limit,k_val))