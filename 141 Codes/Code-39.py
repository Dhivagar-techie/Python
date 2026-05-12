#Transpose of a matrix

matrix=[
    [22,21],
    [32,11],
    [54,23]
]

transporse=[
    [0,0,0],
    [0,0,0]
]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        transporse[j][i]=matrix[i][j]

for row in transporse:
    print(row)