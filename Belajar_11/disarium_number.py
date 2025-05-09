# A Disarium number is a number that is equal to the sum of its digits each raised to the
#  power of its respective position. For example, 89 is a Disarium number because.
#  8^1 + 9^2 = 8 + 81 = 89.

def is_disarium(number):
    # Convert the sum to a string to iterate over each digit
    num_str = str(number)
    
    # Calculate the sum of digits raised to their respective positions
    digit_sum = sum(int(digit) ** (index + 1) for index, digit in enumerate(num_str))
    
    # Check if the sum is equal to the original number
    return digit_sum == number

# Input a number from the users
try:
    num = int(input("Enter a number: "))
    
    # Check if the number is a Disarium number
    if is_disarium(num):
        print(f"{num} is a Disarium number.")
    else:
        print(f"{num} is not a Disarium number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")