
                ### using numpy ###


import numpy as np

# Two matrices using lists
a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]

# Convert lists into NumPy arrays
mat_1 = np.array(a)
mat_2 = np.array(b)

# Addition of two matrices
mat_3 = mat_1 + mat_2

# Display matrices
print("First matrix:")
print(mat_1)

print("Second matrix:")
print(mat_2)

print("Addition of two matrices:")
print(mat_3)



                        ###  using list method ###



matrix1 = [[1, 6, 3],
           [4, 5, 6],
           [7, 8, 13]]

matrix2 = [[9, 8, 7],
           [6, 43, 4],
           [3, 2, 56]]

rows = len(matrix1)
coloumn = len(matrix1[0])

result = []
for i in range(rows):
    row = []
    for j in range(coloumn):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

print("Matrix 1:")
for r in matrix1:
    print(r)

print("Matrix 2:")
for r in matrix2:
    print(r)

print("Addition of two matrices:")
for r in result:
    print(r)



                    ### THANK YOU ###