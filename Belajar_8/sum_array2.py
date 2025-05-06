# Function to find the sum of an array

def sum_of_array(arr):
    total = 0  # Initialize total to 0
    
    for element in arr:
        total += element # Add each element to total
        
    return total  # Return the final sum

# Example usage
array = [1, 2, 3]  # Define an array
sum_result = sum_of_array(array)  # Call the function with the array
print("Sum of array is:", sum_result)  # Print the result