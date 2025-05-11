# Sample list of numbers
numbers = [30, 10, 45, 5, 20]

# Sort the list in descending order
numbers.sort(reverse=True)

# Check if there are at least two elements in the list
if len(numbers) >= 2:
    # The second largest number is the second element in the sorted list
    second_largest_number = numbers[1]
    print("Second largest number in the list:", second_largest_number)
else:
    print("The list does not contain enough elements to find the second largest number.")