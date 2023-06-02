# Dutch National Flag Problem aka Sort an Array of 0s,1s and 2s
limit = int(input())
array = [int(input()) for i in range(limit)]

def sort_zeroes_ones_twos(arr,size):
    left  = 0
    right = size - 1
    i = 0
    while i <= right:
        if arr[i] == 0:
            arr[left],arr[i] = arr[i],arr[left]
            left += 1
            i += 1

        elif arr[i] == 1:
            i += 1

        else:
            arr[right],arr[i] = arr[i],arr[right]
            right -=1
        
    print(arr)


sort_zeroes_ones_twos(array,limit)
            