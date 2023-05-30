# Find maximum ,second maximum and third maximum in array
def max(arr,size):
    for i in range(size-1):
        min_index = i

        for j in range(i+1,size):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            # swapping
            arr[i],arr[min_index] = arr[min_index],arr[i]

    print(arr)   
    print("First Maximum Number is : ",arr[-1])
    print("Second Maximum Number is : ",arr[-2])
    print("Third Maximum Number is : ",arr[-3])


limit = int(input())
array = [int(input()) for i in range(limit)]

max(array,limit)