# Here we wil do operations (obj creation etc) of Class Item
from main import Item

# Testing Getters (read-only)
item1 = Item("MyItem", 750)             # Name setted during obj creation
item1.name = 'Hi'                       # Setting # Changing name after obj creation (If we use getters (@property) This action will be prevented )
print(item1.name)                       # Getting # MyItem (item name doesn't changed even we try to change it as above - due to our getters fn)

# Testing Setters (!read-only)
item1.name = 'Hi'                       # Changing name after obj creation (If we use getters (@property) This action will be prevented)
print(item1.name)                       # Hi # But now we used setters in our item class to overcome that so now we can change the name

