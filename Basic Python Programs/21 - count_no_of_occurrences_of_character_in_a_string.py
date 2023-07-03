# Count the Number of Occurrence of a Character in String
# Method 1 using Collection => Counter
from collections import Counter 

string = 'malayalam'
count = Counter(string)
print(dict(count))


# Method 2 using Dict and Count
string = 'malayalam'
d = {}

for i in string:
    count = string.count(i)
    d[i] = count

print(d)


