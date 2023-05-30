# Check if a string is palindrome
string  = input()
flag = False
for i in range(len(string)):
    if string[i] != string[len(string)-1-i]:
        flag = True
        break

if flag:
    print("Not Palindrome") 
else:
    print("Palindrome") 

########## while ###########
str = input()
length = len(str) - 1
count = 0
flag = False
while count < length:
    if str[count] != str[length]:
        flag = True
        break

    count  += 1
    length -= 1
    
if flag:
    print("Not Palindrome") 
else:
    print("Palindrome") 