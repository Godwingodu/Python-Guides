# Check if a number is prime or not
def prime_number(num):
    # define a flag variable
    flag = False

    if num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True and # break out of loop
                flag = True 
                break

        # check if flag is True
        if flag:
            print(num, "is not a prime number")
        else:
            print(num, "is a prime number")


n = int(input())
prime_number(n)