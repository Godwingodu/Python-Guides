# Rotate Array by k Elements
"""
i/p => [1,2,3,4,5,6,7] : k = 3
o/p => [5,6,7,1,2,3,4]
"""
limit = int(input())
array = [int(input()) for i in range(limit)]
K_val = int(input())

# Reverse code to reduce code repetition make it a fn. This code is repeated thats why .
def reverse(arr,left,right):
        while left < right:
            arr[right],arr[left] = arr[left],arr[right]
            left  += 1
            right -= 1


def reverse_array_by_k(arr,size,k):
    if k < 0 or k >= size:
        return

    reverse(arr,left = 0,right = size-1-k)           # reverse elements from index : 0 to index before 1st kth element : 0 to size-k-1
    
    reverse(arr,left = size-k,right = size-1)        # reverse elements from index : 1st kth element to last kth element : size-k to size-1
    
    reverse(arr,left = 0,right = size-1)             # reverse elements from index : 0 to last element : 0 to size-1 : reverse array completely
  
    print(arr)
  
    
reverse_array_by_k(array,limit,K_val)