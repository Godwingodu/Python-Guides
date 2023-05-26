# HashSet (a.k.a Set)
# Donot Store duplicates | Unordered collection of unique elements.
"""
a = {1,2,3} - defining a set by user
print(a)    - {1, 2, 3}
"""
mySet = set()

mySet.add(1)
mySet.add(2)
mySet.add(3)
print(mySet)            # O/P => {1, 2}

print(len(mySet))       # O/P => 2  |  length

# Check whether a element is in set or not
print(1 in mySet)       # O/P => True
print(2 in mySet)       # O/P => True
print(3 in mySet)       # O/P => False

# Remove a element from a set (without specifying index)
mySet.remove(1)
print(1 in mySet)       # O/P => False

mySet.pop()             # Remove element from left side rather than end (right)

# List to Set
print(set([1,2,3]))     # O/P => {1, 2, 3}

# Set Comprehension
Set = set()
Set = {i for i in range(5)}
print(Set)              # O/P => {0, 1, 2, 3, 4}

# No Duplicates
a = {1,2,3,4,4,4}
print(a)                # O/P => {1, 2, 3, 4}        |  No duplicates allowed, will print a element only once 

# Print list by removing duplicates
b = [1,2,2,2,3,3,4,5,5,6]
b = list(set(b))
print(b)                # O/P => [1, 2, 3, 4, 5, 6]  | No Duplicates 

# Accessing elements in a set (forloop only)
for i in b:
    print(i)
    
"""
Discard same as remove but no error will get when we remove a element that is not in set unlike remove function .

"""



# from collections import Counter
# c = Counter(b)
# print(dict(c))