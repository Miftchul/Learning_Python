#  A Harshad number (or Niven number) is an integer that is divisible by the sum of its digits.
#  In other words, a number is considered a Harshad number if it can be evenly divided by the
#  sum of its own digits.
#  For example:
#  18 is a Harshad number because 
# 1 +8 =9
#  4 +2 =6
#  , and 18 is divisible by 9
#  42 is not a Harshad number because 
# , and 42 is not divisible by 6.

def is_harshad_number(num):
    # Calculate the sum of the digits
    digit_sum = sum(int(digit) for digit in str(num))
    
    # Check if the number is divisible by the sum of its digits
    return num % digit_sum == 0

# Input a number
num = int(input("Enter a number: "))

# Check if the number is a Harshad number
if is_harshad_number(num):
    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is not a Harshad number.")