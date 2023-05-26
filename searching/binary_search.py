# Binary Search
def binary_search(arr,n,find):
    lower = 0
    upper = n-1
    arr.sort()
    while(lower <= upper):
        mid = (lower + upper) // 2
        if find == arr[mid]:
            return mid
        elif find < arr[mid]:
            upper = mid - 1
        else:
            lower = mid + 1
    return -1

limit      = int(input())
array      = [ int(input()) for i in range(limit) ]
target     = int(input())

print(binary_search(array,limit,target))