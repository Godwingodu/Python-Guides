# Print the number series of 14,28,20,40,32,64......... till N terms, N = 10
# 14+14 = 28, 28-8 = 20, 20+20 = 40, 40-8 = 32, 32+32 = 64, 64-8=56
# At odd iteration we add the same number , At even iterations we subtract -8 from the same number 

limit = 10
first_term = 14

def nums(term1,N):
    print(term1,end=' ')
    for i in range(1, N+1):
        if i % 2 == 0:
            term1 -= 8
            print(term1,end=' ')
        else:
            term1 += term1
            print(term1,end=' ')


nums(first_term,limit)