# Function to add two matrices
def add_matrices(mat1, mat2):
    # Check if the matrices have the same dimensions
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        raise ValueError("Matrices must have the same dimensions to be added.")
    
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(mat1[0]))] for _ in range(len(mat1))]
    
    # Add corresponding elements of the matrices
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            result[i][j] = mat1[i][j] + mat2[i][j]
    
    return result  # Return the resulting matrix

# Input matrices
matrix_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Call the add_matrices function and print the result
result_matrix = add_matrices(matrix_1, matrix_2)  # Call the function with the input matrices

# Display the result
if isinstance(result_matrix, str):
    print(result_matrix)  # Print the error message if any
else:
    print("Resulting Matrix:")  # Print the header for the resulting matrix
    for row in result_matrix:
        print(row)