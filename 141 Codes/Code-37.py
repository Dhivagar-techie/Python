# Adding two matrices

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

result = [
    [0, 0],
    [0, 0]
]

# Matrix addition
for i in range(len(A)):

    for j in range(len(A[0])):

        result[i][j] = A[i][j] + B[i][j]

# Print result
for row in result:
    print(row)