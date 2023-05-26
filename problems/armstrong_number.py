# Check a number is armstrong or not
# 153 = 1**3 + 5**3 + 3**3 , where 3 => count of digits in num

def armstrong(num):                         # 153
    temp        = num                       # Store num in a temp variable
    digit_count = 0                         # Count of digit
    sum         = 0                         # Sum of digit 
    while num > 0:                          # while loop to get count of digit
        digit_count += 1                    # In each iteration increment digit count by 1
        num = num // 10

    num = temp                              # After loop break the orginal num value will become 0 so we have to use this num
                                            # for next loop also, so for that we had stored orginal num in temp so we can get it from there as num = temp
    
    while num > 0:                          # While loop for getting sum of  digit**digit_count
        digit = num % 10                    # Get each digit
        sum  += digit**digit_count          # Peform digit**digit_count and will add its result to the sum variable
        num = num // 10                     # Reducing the num as before
                                            # After this while loop completion the sum var will have the o/p of 1**3 + 5**3 + 3**3
    if sum == temp:                         # Check if orginal num == sum ; 153 == 1**3 + 5**3 + 3**3 ?
        print('Number is Armstrong')
    else:
        print('Number is not Armstrong')


n = int(input())
armstrong(n)