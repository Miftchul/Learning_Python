# Natural numbers are a set of positive integers that are used to count and order objects.
#  They are the numbers that typically start from 1 and continue indefinitely, including all the
#  whole numbers greater than 0. In mathematical notation, the set of natural numbers is often
#  denoted as "N" and can be expressed as: N = {1, 2, 3, 4, 5, 6, 7, 8, ...}

limit = int(input("Enter the limit: "))

# Initialize the sum
sum = 0

# Use a for loop to iterate through the natural numbers from 1 to the limit
for i in range(1, limit + 1):
    # Add each number to the sum
    sum += i
    
# Print the result
print(f"The sum of natural numbers from 1 to {limit} is: {sum}")