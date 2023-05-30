# First n Fibonacci numbers
# Initialize the first two Fibonacci numbers
fibonacci_num1 = 0
fibonacci_num2 = 1
# Counter to keep track of the generated numbers
count = 1
# Get the number of Fibonacci numbers to generate from the user
n = int(input("Enter the number of Fibonacci numbers to generate: "))
print("Fibonacci series:", end=' ')
while count <= n:
    # Print the current Fibonacci number
    print(fibonacci_num1, end=' ')
    # Calculate the next Fibonacci number
    next_num = fibonacci_num1 + fibonacci_num2
    # Update the values for the next iteration
    fibonacci_num1 = fibonacci_num2
    fibonacci_num2 = next_num
    # Increment the counter
    count += 1



#Python program to generate Fibonacci series Program using Recursion
def fibonacciSeries(Number):
    if(Number == 0):
        return 0
    elif(Number == 1):
        return 1
    else:
        return (fibonacciSeries(Number - 1) + fibonacciSeries(Number - 2))


n = int(input())
print("Fibonacci series:", end = ' ')
for n in range(0, n):  
   print(fibonacciSeries(n), end = ' ')
