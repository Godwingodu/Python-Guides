# Print first n prime numbers
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num-1):
        if num % i == 0:
            return False
    return True

def print_first_n_primes(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            print(num, end=' ')
            count += 1
        num += 1


n = int(input("Enter the value of n: "))
print("First", n, "prime numbers:", end=' ')
print_first_n_primes(n)
