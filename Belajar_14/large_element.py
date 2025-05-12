def find_n_largest(numbers, n):
    # Sort the list in descending order
    sorted_numbers = sorted(numbers, reverse=True)
    # Return the first n elements
    return sorted_numbers[:n]

# sample list of numbers
numbers = [30, 10, -45, 5, 20]
# Number of largest elements to find
N = int(input("N = "))

# find the N largest elements
result = find_n_largest(numbers, N)

# Prin N largest elements
print(f"The {N} largest elements in the list are: {result}")