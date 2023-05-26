# Space seperated input list
n = int(input('Enter limit: '))
x = [int(ele) for ele in input().split(' ')]
print(x)

# Line seperated input list
m = int(input('Enter limit: '))
y = [int(input()) for i in range(m)]
print(y)