# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional
#  array. The element value in the i-th row and j-th column of the array should be i*j.
#  Note: i=0,1.., X-1; j=0,1,¡Y-1.
#  Example
#  Suppose the following inputs are given to the program:
#  3,5
#  Then, the output of the program should be:
#  [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

# Input the dimensions of the array
X, Y = map(int, input("Enter two digits (X, Y) separated by a comma: ").split(','))

# Initialize the 2D array
array = [[0 for j in range(Y)] for i in range(X)]

# Fill the array with the product of indices
for i in range(X):
    for j in range(Y):
        array[i][j] = i * j
        
# Print the resulting 2D array
for row in array:
    print(row)