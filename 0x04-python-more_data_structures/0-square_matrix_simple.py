#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matri = matrix.copy()
    for i in range(len(matri)):
        for j in range(len(matri[i])):
            matri[i][j] *= matri[i][j]
    return matri
