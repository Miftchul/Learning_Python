def split_and_add(arr, k):
    if k <= 0 or k >= len(arr):
        return arr  # Return the original array if k is invalid
    
    # Split the array into two parts
    first_part = arr[:k]  # First k elements
    second_part = arr[k:]  # Remaining elements
    
    # Add the first part to the end of the second part
    result = second_part + first_part  # Concatenate the two parts
    
    return result  # Return the modified array

# Tets the function with an example
arr = [1, 2, 3, 4, 5]  # Define an array
k = 3  # Define the split index
result = split_and_add(arr, k)  # Call the function with the array and split index
print(f"Original array: {arr}")  # Print the original array
print(f"Modified array: {result}")  # Print the modified array