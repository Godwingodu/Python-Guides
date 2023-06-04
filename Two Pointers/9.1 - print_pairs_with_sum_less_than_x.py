# Print Pairs With Sum less than X in a sorted Array
"""
X   - 4
i/p - [1,2,3,4]
o/p - (1,2)                                    # No same pairs 
"""
limit = int(input())
array = [int(input()) for i in range(limit)]   # Array should be sorted | no dupes
x_val = int(input())

def print_pairs(arr,size,x):
    left  = 0
    right = size - 1
    while left < right:
        sum = arr[left] + arr[right]
        if sum < x:
            for i in range(left+1,right+1):
                print((arr[left],arr[i]))      # To print same pairs | Use range('left',right+1) 
            left  += 1
        else:
            right -= 1


print_pairs(array,limit,x_val)
