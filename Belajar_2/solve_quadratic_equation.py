# The standard form of a quadratic equation is ax^2 + bx + c = 0
# where a, b and c are real numbers and a ≠ 0.
# The solutions to this quadratic equation is given by: (−𝑏 ± (b^2 −4𝑎𝑐^1/2 )/(2𝑎)

import math

#Input coefficients a, b and c
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

#Calculate the discriminant
discriminant = b**2 - 4*a*c

#Check if the discriminant is positive, negative or zero
if discriminant > 0:
    # Two real and distint roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
elif discriminant == 0:
    # One real root (double root)
    root = -b / (2*a)
    print(f"Root: {root}")
else:
    # Complex roots
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-discriminant) / (2*a)
    root1 = complex(real_part, imaginary_part)
    root2 = complex(real_part, -imaginary_part)
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")