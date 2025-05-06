def find_large_element(arr):
    if not arr:
        return None  # Return None if the array is empty
    
    # Initialize the largest element to the first element of the array
    largest_element = arr[0]
    
    # Iterate through the array to find the largest element
    for element in arr:
        if element > largest_element:
            largest_element = element  # Update the largest element if a larger one is found
            
    return largest_element  # Return the largest element found in the array

# Example usage
my_array = [10, 20, 30, 99]  # Define an array
result = find_large_element(my_array)  # Call the function with the array
print(f"The largest element in the array is: {result}")  # Print the result

