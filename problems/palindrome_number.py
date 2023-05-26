# Check a number is palindrome or not

def palindrome(num):          # 123
    temp = num                # Store the orginal num in a temp variable # temp = 123
    r = 0                     # Initialize a var r as zero
    while num > 0:            # Checks the num > 0 # 123 > 0
        digit = num % 10      # Extract digit from num using modulos | we will get digits from RtoL(backwards) # 3
        r = r * 10 + digit    # Use this (r*10+digit) # [0+3, r=3], # [30+2, r=32], # [320+1, r=321] 
        num = num // 10       # After that floor divide the num by 10 so we get , num without the extracted digit (3) # 12
                              # Then loop will check conditon is num > 0 # (12>0) then this steps will repeat untill, when then num become 0 
                              # r = 321 (reversed after loop execution)

    if temp == r:             # Check if temp (orginal num) == r (reversed num)   # 123 == 321?    
        print('Number is Palindrome')
    else:
        print('Number is not Palindrome')


n = int(input())    
palindrome(n)