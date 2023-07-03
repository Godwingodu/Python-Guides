"""
Strings are similar to array but they are immutable .
"""
string = 'Hello'
print(string[1])   # O/P => e

# Length
print(len(string)) # O/P => 5

# Immutable
# string[0] = "A" - # error

# Add string to end of a string
string += 'World'
print(string)

# Valid numeric Strings can be converted
print(int('123') + int('321')) # O/P => 444 | Addition 

# Numbers can converted to Strings
print(str(123) + str(321))     # O/P => 123321  | Concating

# Combine a list of strings (with an empty string delimitor)
strings = ['ab', 'cd', 'ef']
print(''.join(strings))        # O/P => abcdef | converted string in a list to a string 

# Slicing similar to list
print(string[::-1])            # O/P => reverse

# Ascii Value
print(ord('A'))                # O/P => 65

# String Comparison
"""
Strings are compared based on ascii values. If 2 string hello and hi , here it will compare ascii of 1st letter from both word since
its same it will then look (compare) for the ascii of 2nd letter of both words and give true or false .
If the string is like Hello & HelloWorld - then comparison will be based on length of the string .

"""

# Split
a = 'Hello World'
print(a.split(' ',maxsplit=1))        # O/P => ['Hello', 'Word'] | split and return list with words based on whitespace

# Replace | a.replace('letter','replace','count')
print(a.replace('l','a'))             # O/P => Heaao Worad       | replacing character in a string

# Find    | a.find('letter','start','end')
print(a.find('H'))                    # O/P => 0                 | return the index of specified character and return it, otherwise return -1
print(a.find('W',4,7))                # O/P => 6                 | return the index of specified character in specified index limit (start,end) 

# Other Methods
a.lower()
a.upper()
a.capitalize()
a.startswith()
a.endswith()


'''
Strings cannot be sorted using .sort() method like lists, for sorting string directly use sorted('string_name') method instead .

or

my_str = "Hello this Is an Example With cased letters"
words = [word.lower() for word in my_str.split()]        # String to list
words.sort()
new_str = ' '.join(words)                                # List back to String
print(my_str)
print(new_str)
'''
