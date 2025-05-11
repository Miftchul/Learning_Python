# Sample list of numbers
numbers = [10, 20, 30, -40, 50]

# Initialize a variable to store the smallest number
minimum_number = numbers[0]

# Iterate through the list and find the smallest number
for i in numbers:
    if i < minimum_number:
        minimum_number = i
        
# Print the smallest number
print("Smallest number in the list:", minimum_number)