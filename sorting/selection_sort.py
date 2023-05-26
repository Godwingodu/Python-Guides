# Selection Sort

def selection_sort(arr,n):
    for i in range(n-1):                            # loops from index 0 to second last element (n-2), coz if we include last index too then at last iteration there will be only one element left to search or sort by the time the arr will be sorted
        lower = i                                   # initially consider index 0 as lower 
        for j in range(lower+1,n):                  # from index 1 to last index 
            if arr[j] < arr[lower]:                 # checks whether any element smaller than the element at index 0 as we assign like that above
                lower = j                           # if so then assign that elemnt's index as lower 
        if lower != i:                              # now we check if the index of the new lower element stored in (lower) is != the orginal index (i) that we 1st assigned as i (j != i)
            # swapping                              # if != then swap index 0 arr[i] of array with new lower ele - arr[lower] and move the ele in index 0 to this new lower elements index i.e arr[lower]
            # temp        =  arr[i]
            # arr[i]      =  arr[lower]
            # arr[lower]  =  temp 
            arr[i], arr[lower] = arr[lower], arr[i] # swapping
    
    return arr

limit      = int(input())
array      = [ int(input()) for i in range(limit) ]

print(selection_sort(array,limit))