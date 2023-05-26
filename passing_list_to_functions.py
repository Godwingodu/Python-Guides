# List can be passed as a param to function as normal like we pass variables

def fun(li):
    li[0] = 0
    print(li)

l = [1,2,3,4]
print(l)
fun(l) 