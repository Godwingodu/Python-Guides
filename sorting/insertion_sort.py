def insertion_sort(arr,size):
    for i in range(1,size):                         # Loops from index 1 to last element,  we dont include index 0th ele coz, we assume ele at index 0 as sorted at first
        key   = arr[i]                              # Stores second element in a variable name key and compare it with elements behind in it (elements present upto this elements index)
        index = i - 1                               # Steps basically defines how many time loop should run, when i = 1, index = 0 - (loop will run one time) | also using this index we can get the element, present before the ele in key
        while ( index >= 0 and  key < arr[index] ): # Checks if index>=0 and ele in key < element present before the element in key (if both conditon true loop works otherwise breaks) | eg- when loop executes 1st time and reaches index-=1, index become -1 then loop will exit there
                                                    # Compare key with each element on the left of it until an element smaller than it is found
                                                    # For descending order, change key < array[index] to key > array[index].         
            arr[index + 1] = arr[index]             # Assigns the element in index to (index + 1)th position [shift] since ,ele in key < element present before the element in key
            index -= 1                              # Reduce the index by 1 (this is to get each ele from RtoL before the key, one by one and to [compare with the key]) and to break the loop too
        arr[index + 1] = key                        # When loop breaks, we will get the correct index to store the element stored in the [key] and will be placed in its correct index by the time

    return arr


limit      = int(input())
array      = [ int(input()) for i in range(limit) ]

print(insertion_sort(array,limit))
