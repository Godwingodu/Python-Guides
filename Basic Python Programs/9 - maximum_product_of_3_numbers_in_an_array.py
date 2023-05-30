# Maximum product of 3 numbers in an array
def max_product(arr,size):

    first_max = second_max = third_max = float('-inf')  # when comparing arr[i] > 1stmax to make arr[i] greater we use -ve inf | arr[i] always > -ve no.
    first_min = second_min = float('inf') # when comparing arr[i] < 1stmin to make arr[i] least we use +ve inf | arr[i] always < +ve inf no.

    for i in range(size):
        # Update maximum values
        if arr[i] > first_max:
            third_max = second_max
            second_max = first_max
            first_max = arr[i]

        elif arr[i] > second_max:
            third_max = second_max
            second_max = arr[i]

        elif arr[i] > third_max:
            third_max = arr[i]
        # Update minimum values
        if arr[i] < first_min:
            second_min = first_min
            first_min = arr[i]

        elif arr[i] < second_min:
            second_min = arr[i]     
        
        # This problem can have 2 solution 1st set for +ve only no. 2nd set come when -ve numbers come so 2 neg no. is positive so its handled below
    return max((first_max*second_max*third_max),(first_min*second_min*first_max))
        
    # print('max',first_max,second_max,third_max)
    # print('min',first_min,second_min)



n = int(input())
array = [int(input()) for i in range(n)]
print(max_product(array,n))


"""
first_max, second_max, and third_max are initialized with negative infinity to store the maximum values.
first_min and second_min are initialized with positive infinity to store the minimum values.
The loop iterates through the array.
If the current element is greater than first_max, the values of first_max, second_max, and third_max are updated accordingly.
If the current element is greater than second_max but not greater than first_max, the values of second_max and third_max are updated.
If the current element is greater than third_max but not greater than second_max, the value of third_max is updated.
Similarly, if the current element is less than first_min, the values of first_min and second_min are updated.
If the current element is less than second_min but not less than first_min, the value of second_min is updated.
Finally, the maximum product is calculated by comparing the products of the maximum and minimum values, and the result is returned.

"""