#  The natural logarithm, often denoted as , is a mathematical function that represents the
#  logarithm to the best e, where e is the base of the natural logarithm, approximately equal to 2.71828.
# In the world, for a positive number x, the natural logaritm of x is the exponent y theat satisfies the equals e^y = x
# Mathematicaly, it is defined as: In(x)
# It is commonly used in various branches of mathematics, especially in calculus and
#  mathematical analysis, as well as in fields such as physics, economics, and engineering.
#  The natural logarithm has properties that make it particularly useful in situations involving
#  exponential growth or decay.

import math
num = float(input("Enter a positive number: "))
if num <= 0:
    print("Sorry, natural logarithm is not defined for non-positive numbers")
else:
    # calculate the natural logarithm
    result = math.log(num)
    print(f"The natural logarithm of, {num}, is, {result}")