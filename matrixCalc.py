#!/usr/bin/env python

"""

"""
import csv
import io
import numpy as np
def loadA():
	file = 'A.csv'
        with io.open(file, 'r', encoding = 'utf-8-sig') as csvfile:
            data = []
	    csv_reader = csv.reader(csvfile, delimiter = ',')
	    for row in csv_reader:
    		data.append(row)
            for i in range(0,len(data)):
                for j in range(0, len(data[0])):
                    try:
                        data[i][j] = int(data[i][j])
                    except ValueError:
                        print("\n ERROR: trying to load a non integer into matrix")
                        return [None]
	    return data

	
def loadB():
	file = 'B.csv'
	with io.open(file, 'r', encoding = 'utf-8-sig') as csvfile:
	    data = []
	    csv_reader = csv.reader(csvfile, delimiter = ',')
	    for row in csv_reader:
	    	data.append(row)
            for i in range(0,len(data)):
                for j in range(0,len(data[0])):
                    try:
                        data[i][j] = int(data[i][j])
                    except ValueError:
                        print("\n ERROR: trying to load a non integer into matrix")
	    return data

def matrixMult(matrix1, matrix2):
    result = [[0 for col in range(len(matrix2[0]))] for rows in range(len(matrix1))] 
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

def transpose(matrix):
    newMatrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return newMatrix

def cofactor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

def cofactornorec(matrix, i, j):
    submat = [[None] * (len(matrix)-1) for x in range(len(matrix)-1)]
    subrow = 0
    subcol = 0
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix)):
            if(row != i and col != j):
                submat[subrow][subcol] = matrix[row][col]
                subcol += 1
                if(subcol == (len(matrix)-1)):
                    subcol = 0
                    subrow += 1
                
    return submat

def determinant(matrix):
    if(len(matrix) == 2):
        det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return det
    
    detSum = 0
    
    for currentColumn in range(len(matrix)):
        sign = (-1) ** (currentColumn)

        subDet = determinant(cofactor(matrix, 0, currentColumn))

        detSum += (sign * matrix[0][currentColumn] * subDet)

    return detSum

def adjoint(matrix):
    adj = [[None]*len(matrix) for _ in range(len(matrix))]
    if(len(matrix) == 1):
        adj = [1]
        return adj

    sign = 1

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if((i+j)%2 == 0):
                sign = 1
            else:
                sign = -1
            adj[j][i] = sign * determinant(cofactornorec(matrix, i, j))

    return adj

def inverse(matrix):
    det = determinant(matrix)

    adj = adjoint(matrix)
    inverse = [[None] * len(matrix) for _ in range(len(matrix))] 
    for i in range(len(adj)):
        for j in range(len(adj)):
            inverse[i][j] = adj[i][j]/float(det)
    return inverse

def constMult(matrix, n):
    result = [[None] * len(matrix) for _ in range(len(matrix))]
    
    for i in range(len(result)):
        for j in range(len(result)):
            result[i][j] = matrix[i][j] * n
    return result

def matrixPower(matrix, power):
    if(power == 1):
        return matrix

    powerMatrix = [[None] * len(matrix) for _ in range(len(matrix))]
    powerMatrix = matrixMult(matrix, matrix)

    for _ in range(0, power-2):
        powerMatrix = matrixMult(matrix, powerMatrix)

    return powerMatrix

def toIdentity(size):
    if(size == 1):
        return [1]

    identity = [[0 for i in range(size)] for j in range(size)]

    for i in range(len(identity)):
        for j in range(len(identity)):
            if(i == j):
                identity[i][j] = 1
    return identity

def toIdentityA(size):
    global aData
    aData = toIdentity(size)
    return

def toIdentityB(size):
    global bData
    bData = toIdentity(size)
    return

def addMatrix(matrix1, matrix2):
    addedMat = [[0 for i in range(len(matrix1))] for j in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            addedMat[i][j] = matrix1[i][j] + matrix2[i][j]
    return addedMat

def subMatrix(matrix1, matrix2):
    subbedMat = [[0 for i in range(len(matrix1))] for j in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            subbedMat[i][j] = matrix1[i][j] - matrix2[i][j]
    return subbedMat

def copyAtoB():
    global aData
    global bData
    bData = aData
    return

def copyBtoA():
    global aData
    global bData
    aData = bData
    return

def swapAandB():
    global aData
    global bData
    temp  = bData
    bData = aData
    aData = temp
    return


inp = 3000

while inp != 0:
    print("\nMATRIX CALCULATOR")
    print("1. Load A")
    print("2. Load B")
    print("3. Make A a square identity matrix: A to I")
    print("4. Make B a square identity matrix: B to I")
    print("5. A times n (will be prompted for n)")
    print("6. B times n (will be prompted for n)")
    print("7. Determinant of A")
    print("8. Determinant of B")
    print("9. Transpose A")
    print("10. Transpose B")
    print("11. Inverse of A")
    print("12. Inverse of B")
    print("13. A + B")
    print("14. B - A")
    print("15. A - B")
    print("16. A * B")
    print("17. B * A")
    print("18. B = A")
    print("19. A = B")
    print("20. Swap A and B")
    print("0. Exit Calculator")
    
    try:
        inp = int(input("\nSelect your choice: "))
    except:
        print("\n ERROR: The value inputted must be a number, nothing else!")
        inp = 3000

    if(inp == 1):
        try:
            aData = loadA()
            print("A: ")
            print(np.matrix(aData))
        except:
            print("No A.csv file is in directory")
    elif(inp == 2):
        bData = loadB()
        print("B: ")
        print(np.matrix(bData))

    

