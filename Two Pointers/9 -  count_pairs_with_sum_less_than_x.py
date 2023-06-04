# Count Pairs With Sum less than X in a sorted Array
"""
X   - 4
i/p - [1,2,3,4]
o/p - 1 (one pair only) 
"""
limit = int(input())
array = [int(input()) for i in range(limit)]   # Array should be sorted | no dupes
x_val = int(input())

def count_pairs(arr,size,x):
    left  = 0
    right = size - 1
    count = 0
    while left < right:
        sum = arr[left] + arr[right]
        if sum < x:
            count += right - left               # Count of pairs that can have sum < x with max right val and given left val | Use 'right-left+1' to inculde same pairs also
            left  += 1
        else:
            right -= 1
        
    print('count :',count)


count_pairs(array,limit,x_val)
