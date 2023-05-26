# Hashmap (a.k.a Dict)
myDict = {}
myDict['sahal'] = 20
myDict['rishal'] = 17
print(myDict)                    # O/P => {'sahal': 20, 'rishal': 17}

print(len(myDict))               # O/P => 2

# Getting Values
print((myDict['rishal']))        # O/P => 17
print((myDict.get('sahal')))     # O/P => 20
"""
myDict.get('key', None)
Here, if there is no value in the given key then the second argument None will display .

"""

# Mutable 
myDict['sahal'] = 22
print(myDict)                    # O/P => {'sahal': 22, 'rishal': 17}

# Membership 
print("sahal" in myDict)         # O/P => True

# Poping    |   myDict.pop('key') 
myDict.pop('rishal')       
print(myDict)                    # O/P => {'sahal': 22}

# Normal initialization
Dict = {'sahal':10,'rishal':5}

# Dict Comprehension
Map = {i:i*2 for i in range(5)}  
print(Map)                       # O/P => {0: 0, 1: 2, 2: 4, 3: 6, 4: 8} 

# Looping through Maps
"""
for key in Map:
    print(key)                   # O/P => all keys

for value in Map.values():
    print(value)                 # O/P => all values
"""
# Key and Value
for key in Map:
    print(key, Map[key])         # O/P => key , value 

for key, value in Map.items():
    print(key, value)            # O/P => key , value 

# Other Methods
print(Map.keys())
print(Map.values())
print(Map.items())
"""
dict_keys([0, 1, 2, 3, 4])
dict_values([0, 2, 4, 6, 8])
dict_items([(0, 0), (1, 2), (2, 4), (3, 6), (4, 8)])

"""
Map.copy()                       # Create a copy of a dict and changes made in the copy_dict will not affect the orginal dict

# Clear & Delete
a = {1:2,2:3,3:0}
a.clear()
print(a)                         # O/P => {}   |  Clears the dictionary 

# del a                          # Deletes the variable itself that stored the dict 

# Update  |  Like appending in list
b = {1:'a',2:'b',3:'c'}
c = {4:'d'}
b.update(c)
print(b)                         # O/P => {1: 'a', 2: 'b', 3: 'c', 4: 'd'}   |  basically appends dict c to b
