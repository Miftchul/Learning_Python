# Function to multiply two matrices

def multiply_matrices(mat1, mat2):
    # Determine the dimensions of the matrices
    rows_mat1 = len(mat1)
    cols1_mat1 = len(mat1[0])
    rows2_mat2 = len(mat2)
    cols2_mat2 = len(mat2[0])
    
    # Check if multiplication is possible
    if cols1_mat1 != rows2_mat2:
        return "Matix multiplication is not possible. Number of columns"
    
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols2_mat2)] for _ in range(rows_mat1)]
    
    # Perform matrx multiplication
    for i in range(rows_mat1):
        for j in range(cols2_mat2):
            for k in range(cols1_mat1):
                result[i][j] += mat1[i][k] * mat2[k][j]
                
    return result

# Example matrix
matrix1 = [[1, 2, 3],[4, 5, 6]]
matirx2 = [[7, 8],[9, 10],[11, 12]]

# Multiple the matrix 
result_matrix = multiply_matrices(matrix1, matirx2)

# Display the result
if isinstance(result_matrix, str):
    print(result_matrix)
else:
    print("Resultant matrix:")
    for row in result_matrix:
        print(row)