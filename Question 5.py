//matrices//

A ← [[18, 17, 3],
     [4, 5, 6],
     [7, 8, 11]]

B ← [[5, 8, 1,12],
     [6,7, 3, 0],
     [14, 4, 9, 1]]

MATRIX ← [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

//pseudocode for addition//
for I in range(len(A)): //iterates through rows//
     for j in range(len(A[0])): //iterates through columns//
        MATRIX[i][j] ← A[i][j] + B[i][j]

for m in matrix:
    print(m)

//pseudocode for subtraction
for I in range(len(A)): //iterates through rows//
    for j in range(len(A[0])): //iterates through columns//
        MATRIX[i][j] ← A[i][j] – B[i][j]

for m in MATRIX:
    print(m)

//pseudocode for multiplication
for I in range (len(A)): //iterate through rows of A//
    for j in range (len(B[0])): //iterate through columns of B//
        for k in range (len(B)): //iterate through rows of B//
            result[i][j] +← A[i][k] * B[k][j]

for m in MATRIX:
    print (m)
