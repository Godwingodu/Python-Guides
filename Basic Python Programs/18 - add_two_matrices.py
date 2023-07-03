# Add Two Matrices
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

S = [[0,0,0],
    [0,0,0],
    [0,0,0]]

for i in range(len(X)):
    for j in range(len(X)):                # len(X[i]) jagged list
        # print(X[i][j])
        # print(Y[i][j])
        S[i][j] += X[i][j] + Y[i][j]
    
print(S)

    
    