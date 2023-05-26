"""
Break Statement is used to exit from a loop when a particular condition is met .

"""

for i in range(10):
    if i == 5:
        break
    print(i)
print('loop exited')

"""
Continue Statement is used to skip an iteration while looping when a particular condition is met .

"""
# print numbers from 1 to 5 , but don't print 3
for i in range(1,6):
    if i == 3:
        continue
    print(i)