def linear_search(arr,n,v):
    for i in range(n):
        if arr[i] == v:
            print(i)
        else:
            print(-1)

# x = [int(ele) for ele in input().split()]
# s = len(x)
# f = int(input())

limit = int(input())
a     = [int(input()) for i in range(limit)]
value = int(input())

# linear_search([1,2,3,4],4,4)
# linear_search(arr=x,n=s,v=f)
linear_search(a,limit,value)


