# Armstrong Number:
# An Armstrong number is a number that is equal to the sum of its own digits, 
# each raised to the power equal to the number of digits in the number.

# For example, consider the number 153:
# - It has three digits: 1, 5, and 3.
# - If we calculate 1^3 + 5^3 + 3^3, we get 1 + 125 + 27 = 153.
# - Therefore, 153 is an Armstrong number.

# Another example is 9474:
# - It has four digits: 9, 4, 7, and 4.
# - If we calculate 9^4 + 4^4 + 7^4 + 4^4, we get 6561 + 256 + 2401 + 256 = 9474.
# - Therefore, 9474 is also an Armstrong number.

num = int(input("Enter a number: "))

# Calculate the number of digits in num
num_str = str(num)
num_digits = len(num_str)

# Initialize variables
sum_of_powers = 0
temp_num = num

# Calculate the sum of digits raised to the power of num_digits
while temp_num > 0:
    digit = temp_num % 10
    sum_of_powers += digit ** num_digits
    temp_num //= 10

# Check if it's an Armstrong number
if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")