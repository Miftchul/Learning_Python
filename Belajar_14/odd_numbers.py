# Sample list of even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using list comprehension to find odd numbers
even_numbers = [num for num in numbers if num % 2 != 0]

# Print the odd numbers
print("Odd numbers in the list:", even_numbers)