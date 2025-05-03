# Least Common Multiple (LCM):
#  LCM, or Least Common Multiple, is the smallest multiple that is exactly divisible by two or
#  more numbers.
#  Formula:
#  For two numbers a and b, the LCM can be found using the formula:
#  LCM(a, b) = (a * b) / GCD(a, b)
#  where GCD is the Greatest Common Divisor of a and b.

# For more than two numbers, you can find the LCM step by step, taking the LCM of pairs of
#  numbers at a time until you reach the last pair.
#  Note: GCD stands for Greatest Common Divisor.

# Python program to find the LCM of two numbers

def computer_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
    return lcm

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The LCM of", num1, "and", num2, "is", computer_lcm(num1, num2))
# The LCM of 12 and 15 is 60