# Arrays (called lists in python)
arr = [1,2,3]
print(arr)

# Can be used as a stack [LIFO]
arr.append(4) # append as last element 
arr.append(5) 
print(arr)

arr.pop()  # pop last element by default
arr.pop(2) # pop using index
arr.remove(1) # remove element by specifying element itself
print(arr)

# Insert element at specified index
arr.insert(1,11)
print(arr)

# other way
arr[0] = 0
arr[1] = 1
print(arr)

# Find Index of element
print(arr.index(4))

# Initialize an array of size n with default value of 1 
# When multiply an array with a value
n = 5
x = [1]*n
print(x) # O/P => [1, 1, 1, 1, 1]

x = [1,2,3]*5
print(x) # O/P => [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

# Indexing
print(arr[1])  # O/P => 1
print(arr[-1]) # O/P => 4

# Sublists or Slicing [start-0:end(n-1):step-1]
y = [1, 2, 3, 4]
print(y[1:3])  # O/P => [2, 3]
print(y[:])    # O/P => [1, 2, 3, 4]
print(y[::-1]) # O/P => [4, 3, 2, 1]  |  Reverse Array Elements

# Unpacking 
a,b,c = [1, 2, 3]
print(a ,b ,c) # O/P => 1 2 3

# Loop through arrays
nums = [1,2,3,4]

# Using index
for i in range(len(nums)):
    print(nums[i])

# Without index
for i in nums:
    print(i)

# With index and value
for i, n in enumerate(nums):
    print(i, n) 
    
    # O/P =>
    """     0 1
            1 2
            2 3
            3 4
    """

# Loop through multiple arrays simultaneously and unpack
nums1 = [2, 4, 6]
nums2 = [1, 3, 5]
for num1, num2 in zip(nums1, nums2):
    print(num1, num2)

    # O/P =>
    """     2 1
            4 3
            6 5
    """

# Reverse an array without slicing
nums1.reverse()
print(nums1)

# Sorting an array
sort_arr = [2, 100, 1, 8, 0]
sort_arr.sort()
print(sort_arr)  # O/P => [0, 1, 2, 8, 100] | Ascending
sort_arr.sort(reverse=True)
print(sort_arr)  # O/P => [100, 8, 2, 1, 0] | Descending

sort_arr_2 = ['sahal','alex','jhon','godu']
sort_arr_2.sort()
print(sort_arr_2) # O/P => ['alex', 'godu', 'jhon', 'sahal'] | Default : Alphabetic Order

# Custom sort by (length of string)
sort_arr_2.sort(key= lambda x:len(x))
print(sort_arr_2) # O/P => ['alex', 'godu', 'jhon', 'sahal'] 

# List Comprehension
array = [i for i in range(10)]
print(array)      # O/P => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

array = [i+i for i in range(10)]
print(array)      # O/P => [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 2-D List
array = [[0]*4 for i in range(5)]
print(array)      # O/P => [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# Print poped element from a list
bc = [1,2]
print(bc.pop(1))

# Extending a List
# Add elements in List B to A
A = [1, 2, 3]
B = [4, 5, 6]
A.extend(B)
print(A)          # O/P => [1, 2, 3, 4, 5, 6]