# Print a given number in reverse manner

def reverse(num):             # 123
    r = 0                     # Initialize a var r as zero
    while num > 0:            # Checks the num > 0 # 123 > 0
        digit = num % 10      # Extract digit from num using modulos | we will get digits from RtoL(backwards) # 3
        r = r * 10 + digit    # Use this (r*10+digit) # [0+3, r=3], # [30+2, r=32], # [320+1, r=321] 
        num = num // 10       # After that floor divide the num by 10 so we get , num without the extracted digit (3) # 12
                              # Then loop will check conditon is num > 0 # (12>0) then this steps will repeat untill, when then num become 0 
    print(r)                  # Then print number stored in r (it will be in reverse manner by the time)
    

n = int(input())    
reverse(n)