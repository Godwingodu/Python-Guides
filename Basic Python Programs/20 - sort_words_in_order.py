# Sort Words in Alphabetic Order
my_str = "Hello this Is an Example With cased letters"

words = [word.lower() for word in my_str.split()]        # String to list
words.sort()

new_str = ' '.join(words)                                # List back to String

print(my_str)
print(new_str)