# Sum of numbers in array
def sum_of_array(arr):
    sum = 0
    for ele in arr:
        sum += ele
    print(sum)


limit = int(input())
array = [int(input()) for i in range(limit)]

sum_of_array(array)