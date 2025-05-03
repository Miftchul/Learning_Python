# Highest Common Factor(HCF):
#  HCF, or Highest Common Factor, is the largest positive integer that divides two or more
#  numbers without leaving a remainder.
#  For two numbers a and b, the HCF can be found using the formula:
#  HCF(a, b) = (a * b) / LCM(a, b)

# For more than two numbers, you can find the HCF by taking the GCD of pairs of numbers at
#  a time until you reach the last pair.
#  Note: GCD stands for Greatest Common Divisor.

# Python program to find the HCF of two numbers
# define a function

def computer_hcf(x, y):
    # Choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    # Iterate from 1 to the smaller number
    for i in range(1, smaller + 1):
        # Check if i divides both x and y
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The HCF of", num1, "and", num2, "is", computer_hcf(num1, num2))
# The HCF of 12 and 15 is 3
