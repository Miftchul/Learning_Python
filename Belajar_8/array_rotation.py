def rotate_array(arr, d):
    n = len(arr)  # Get the length of the array

    # Check if the array is empty or if d is 0
    if d < 0 or d >= n:
        return "Invalid rotation count"  # Return an error message if d is invalid

    # Perform the rotation using slicing
    d = d % n  # Handle cases where d > n
    rotated_arr = arr[d:] + arr[:d]  # Rotate the array using slicing

    return rotated_arr  # Return the rotated array

# Input array and rotation count
arr = [1, 2, 3, 4, 5]  # Define an array
# Number of positions to rotate
d = 2  # Define the number of positions to rotate

# Call the function and print the result
result = rotate_array(arr, d)  # Call the function with the array and rotation count

print(f"Original array: {arr}")  # Print the original array
print(f"Rotated array: {result}")  # Print the rotated array
