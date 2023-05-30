# Print even and odd numbers in a range
lower_limit = int(input())
upper_limit = int(input())
print('Even : ',end=' ')
# print('Odd : ',end=' ')
def even_odd(lower,upper):
    for i in range(lower,upper+1):
        if i % 2 == 0:
            print(i,end=' ')
        # else:
        #     print(i,end=' ')


even_odd(lower_limit,upper_limit)