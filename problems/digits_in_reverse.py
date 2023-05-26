# Print digits of a given number in reverse manner

def reverse(num):             # 123
    while num > 0:            # Checks the num > 0 # 123 > 0
        digit = num % 10      # Extract digit from num using modulos | we will get digits from RtoL(backwards) # 3
        print(digit)          # Then print the digit we extracted # 3
        num = num // 10       # After that floor divide the num by 10 so we get , num without the extracted digit (3) # 12
                              # Then loop will check conditon is num > 0 # (12>0) then this steps will repeat untill, when then num become 0 

n = int(input())    
reverse(n)