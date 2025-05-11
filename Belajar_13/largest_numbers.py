# Sample largest numbers
numbers = [30, 10, -45, 5, 20]
# Initialize a variable to store the largest number
largest_number = numbers[0]
# Iterate through the list and find the largest number
for i in numbers:
    if i > largest_number:
        largest_number = i
# Print the largest number
print("Largest number in the list:", largest_number)