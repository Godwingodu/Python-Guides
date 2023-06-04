# Container with most water
"""
Basically what we have to do is find to lines take min from these 2 lines (breadth) and join these min line to the other line vertically
these distance b/w these lines (length). Then find its area, such that we have to return max area that 2 lines can have . 
"""
limit = int(input())
array = [int(input()) for i in range(limit)]   # Array should be sorted | no dupes | if not sorted sort it

def max_area(arr,size):
    left  = 0
    right = size - 1
    max_val = float('-inf')                    # Define a initial value for max : -inf
    while left < right:
        first   = arr[left]                    # Storing line value
        second  = arr[right]
        max_val = max(max_val, min(first,second) * (right-left))   # find area l*b : min(f,s) => breadth, (r-1) => length (distance b/w 2 lines index points) 

        if first < second:
            left  += 1
        else:
            right -= 1

    print(max_val)


max_area(array,limit)