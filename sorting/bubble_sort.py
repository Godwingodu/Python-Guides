def bubble_sort(arr,size):
    for i in range(size-1):                              # loops from index 0 to second last element (n-2), coz if we include last index too then at last iteration there will be only one element left to search or sort by the time the arr will be sorted
        for j in range(size-1,i,-1):                     # loops bottom to top without including the ith index it will loop from last index to i+1 in each iteration the index will be reduced by -1 as it move upwards
            if arr[j] < arr[j-1]:                        # checks if last element < second last ele if so swap | used for ascending sort
            # if arr[j] > arr[j-1]:                      # checks if last element > second last ele if so swap | used for descending sort
                # swapping
                arr[j],arr[j-1] = arr[j-1],arr[j]
    
    return arr


limit      = int(input())
array      = [ int(input()) for i in range(limit) ]

print(bubble_sort(array,limit))