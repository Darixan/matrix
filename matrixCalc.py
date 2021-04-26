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
                    data[i][j] = int(data[i][j])
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
                    data[i][j] = int(data[i][j])
	    return data
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


aData = loadA()
bData = loadB()

print(np.matrix(aData))
print(np.matrix(bData))
length = len(aData)
print(length)
det = determinant(aData)
adjointA = adjoint(aData)
print(np.matrix(adjointA))
