# Find maximum number in an array
def max_of_array(arr):
    max = 0
    for ele in arr:
        if ele >= max:
            max = ele

    print("Largest Number is : ",max)


limit = int(input())
array = [int(input()) for i in range(limit)]

max_of_array(array)