#!/usr/bin/env python

"""
Written By: Terry Watson
CMPS 3500
Project: Matrix Calculator
Description: Used in pair with A.csv and B.csv to perform calculations on the contained
matrices
"""
import csv
import io
import numpy as np
"""
loadA() and loadB() are essentially the same function. They load their respective CSV files
and do some error testing on the data to make sure it can be properly processed.
"""
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
"""
matrixMult takes two matrices and find the multiplication of the two
"""
def matrixMult(matrix1, matrix2):
    result = [[0 for col in range(len(matrix2[0]))] for rows in range(len(matrix1))] 
    #k is used to iterate through the entire column for each row
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

"""
transpose swaps a matrix along its diagonal from the top left to bottom right of the matrix
"""
def transpose(matrix):
    newMatrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return newMatrix

"""
cofactor finds the submatrix of a given point at i, j
"""
def cofactor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
"""
The above cofactor only works when working in a recursive way for determinant.
This cofactor function can find the submatrix regardless of original point
"""
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

"""
determinant recursively finds the scalar discriminant of a matrix with a base case of a 2x2 matrix
"""
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
"""
adjoint find the adjoin matrix of a given matrix. It uses the above determinant function to do so.
"""
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

"""
inverse find the inverse matrix of the given matrix.
It uses the above determinant and adjoint functions to do so.
"""
def inverse(matrix):
    det = determinant(matrix)

    adj = adjoint(matrix)
    inverse = [[None] * len(matrix) for _ in range(len(matrix))] 
    for i in range(len(adj)):
        for j in range(len(adj)):
            inverse[i][j] = adj[i][j]/float(det)
    return inverse

"""
constMult finds a scalar multiple of a given matrix
"""
def constMult(matrix, n):
    result = [[None] * len(matrix) for _ in range(len(matrix))]
    
    for i in range(len(result)):
        for j in range(len(result)):
            result[i][j] = matrix[i][j] * n
    return result

"""
matrixPower uses matrixMult from above to find a given matrix to a certain power n
"""
def matrixPower(matrix, power):
    if(power == 1):
        return matrix

    powerMatrix = [[None] * len(matrix) for _ in range(len(matrix))]
    powerMatrix = matrixMult(matrix, matrix)

    for _ in range(0, power-2):
        powerMatrix = matrixMult(matrix, powerMatrix)

    return powerMatrix

"""
toIdentity creates an identity matrix of a given size.
"""
def toIdentity(size):
    if(size == 1):
        return [1]

    identity = [[0 for i in range(size)] for j in range(size)]

    for i in range(len(identity)):
        for j in range(len(identity)):
            if(i == j):
                identity[i][j] = 1
    return identity

"""
toIdentityA sets A to an identity matrix of the same size.
"""
def toIdentityA(size):
    global aData
    aData = toIdentity(size)
    return

"""
toIdentityB does the same as prior but for B.
"""
def toIdentityB(size):
    global bData
    bData = toIdentity(size)
    return

"""
addMatrix adds two matrices element wise and returns result.
"""

def addMatrix(matrix1, matrix2):
    addedMat = [[0 for i in range(len(matrix1))] for j in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            addedMat[i][j] = matrix1[i][j] + matrix2[i][j]
    return addedMat

"""
submatrix subtracts two matrices element wise and returns result.
"""

def subMatrix(matrix1, matrix2):
    subbedMat = [[0 for i in range(len(matrix1))] for j in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            subbedMat[i][j] = matrix1[i][j] - matrix2[i][j]
    return subbedMat

"""
copyAtoB copies A's data to B
"""

def copyAtoB():
    global aData
    global bData
    bData = aData
    return

"""
copyBtoA copies B's data to A
"""

def copyBtoA():
    global aData
    global bData
    aData = bData
    return

"""
swapAandB swaps the data between A and B
"""
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
    print("13. A ^ n")
    print("14. B ^ n")
    print("15. A + B")
    print("16. B - A")
    print("17. A - B")
    print("18. A * B")
    print("19. B * A")
    print("20. B = A")
    print("21. A = B")
    print("22. Swap A and B")
    print("23. Print A")
    print("24. Print B")
    print("0. Exit Calculator")
    
    try:
        inp = int(input("\nSelect your choice: "))
    except:
        print("\n ERROR: The value inputted must be a number, nothing else!")
        inp = 3000

    if(inp == 1):
        try:
            temp = loadA()
            diffsize = False
            
            for i in range(len(temp)):
                if len(temp[i]) != len(temp[0]):
                    diffsize = True
            
            if(len(temp) > 10 or len(temp[0]) > 10):
                print("Error: Can only load matrices up to size 10x10!")
            elif(diffsize):
                print("Error: Matrix has to be of the same size for each row!")
            else:
                aData = temp
                print("A: ")
                print(np.matrix(aData))
        except IOError:
            print("No A.csv file is in directory")
        except TypeError:
            print("You cannot have foreign symbols. Matrix must be 1x1 - 10x10 and be made of integers")
        except IndexError:
            print("The matrix cannot be an empty matrix!")
    elif(inp == 2):
        try:
            temp = loadB()
            diffsize = False
            
            for i in range(len(temp)):
                if len(temp[i]) != len(temp[0]):
                    diffsize = True

            if(len(temp) > 10 or len(temp[0]) > 10):
                print("Can only load matrices up to size 10x10!")
            elif(diffsize):
                print("Error: Matrix has to be of the same size for each row!")
            else:
                bData = temp
                print("B: ")
                print(np.matrix(bData))
        except IOError:
            print("No A.csv file is in directory")
        except TypeError:
            print("You cannot have foreign symbols. Matrix must be a 1x1 - 10x10 and be made of integers")
        except IndexError:
            print("The matrix cannot be an empty matrix!")
    elif(inp == 3):
        if('aData' in globals()):
            if(len(aData[0]) == len(aData)):
                toIdentityA(len(aData))
                print("A is now: ")
                print(np.matrix(aData))
            else:
                print("A is not a square matrix!")
        else:
            print("Matrix A does not exist, try loading it!")
    elif(inp == 4):
        if('bData' in globals()):
            if(len(bData[0]) == len(bData)):
                toIdentityB(len(bData))
                print("B is now: ")
                print(np.matrix(bData))
            else:
                print("B is not a square matrix!")
        else:
            print("Matrix B does not exist, try loading it!")
    elif(inp == 5):
        if('aData' in globals()):
            try:
                n = int(input("Please input a value for integer n to multiply by: "))
                result = constMult(aData, n)
                print("Result: ")
                print(np.matrix(result))
                choice = raw_input("Would you like to store result to A? (Y for yes, anything else for no): ")
                if(choice == "Y"):
                    aData = result
            except:
                print ("Please input a valid integer!")
        else:
            print("Matrix A does not exist, try loading it!")
    elif(inp == 6):
        if('bData' in globals()):
            try:
                n = int(input("Please input a value for integer n to multiply by: "))
                result = constMult(bData, n)
                print("Result: ")
                print(np.matrix(result))
                choice = raw_input("Would you like to store result to B? (Y for yes, anything else for no): ")
                if(choice == "Y"):
                    bData = result
            except:
                print ("Please input a valid integer!")
        else:
            print("Matrix B does not exist, try loading it!")
    elif(inp == 7):
        if('aData' in globals()):
            if(len(aData[0]) == len(aData)):
                det = determinant(aData)
                print("The determinant is: " + str(det))
            else:
                print("A must be a square matrix!")
        else:
            print("Matrix A does not exist, try loading it!")
    elif(inp == 8):
        if('bData' in globals()):
            if(len(bData[0]) == len(bData)):
                det = determinant(bData)
                print("The determinant is: " + str(det))
            else:
                print("B must be a square matrix!")
        else:
            print("Matrix B does not exist, try loading it!")
    elif(inp == 9):
        if('aData' in globals()):
            result = transpose(aData)
            print("Transposed matrix: ")
            print(np.matrix(result))
        else:
            print("Matrix A does not exist, try loading it!")
    elif(inp == 10):
        if('bData' in globals()):
            result = transpose(bData)
            print("Transposed matrix: ")
            print(np.matrix(result))
        else:
            print("Matrix B does not exist, try loading it!")
    elif(inp == 11):
        if('aData' in globals()):
            if(len(aData[0]) == len(aData)):
                inv = inverse(aData)
                print("The invere matrix for A is: ")
                print(np.matrix(inv))
            else:
                print("A must be a square matrix!")
        else:
            print("Matrix A does not exist, try loading it!")
    elif(inp == 12):
        if('bData' in globals()):
            if(len(bData[0]) == len(bData)):
                inv = inverse(bData)
                print("The invere matrix for B is: ")
                print(np.matrix(inv))
            else:
                print("B must be a square matrix!")
        else:
            print("Matrix B does not exist, try loading it!")
    elif(inp == 13):
        if('aData' in globals()):
            if(len(aData) == len(aData[0])):
                try:
                    n = int(input("Please input a value for exponent n to power by: "))
                    result = matrixPower(aData, n)
                    print("Result: ")
                    print(np.matrix(result))
                except:
                    print ("Please input a valid integer!")
            else:
                print("A must be a square matrix")
        else:
            print("Matrix A does not exist, try loading it!")
    elif(inp == 14):
        if('bData' in globals()):
            if(len(bData) == len(bData[0])):
                try:
                    n = int(input("Please input a value for exponent n to power by: "))
                    result = matrixPower(bData, n)
                    print("Result: ")
                    print(np.matrix(result))
                except:
                    print ("Please input a valid integer!")
            else:
                print("B must be a square matrix")
        else:
            print("Matrix B does not exist, try loading it!")

    elif(inp == 15):
        if('aData' in globals()) and ('bData' in globals()):
            if(len(aData[0]) == len(bData[0])) and (len(aData) == len(bData)):
                result = addMatrix(aData, bData) 
                print("The added matrix is: ")
                print(np.matrix(result))
            else:
                print("A and B must be the same size.")
        else:
            print("Matrix A or B does not exist, try loading it!")
    elif(inp == 16):
        if('aData' in globals()) and ('bData' in globals()):
            if(len(aData[0]) == len(bData[0])) and (len(aData) == len(bData)):
                result = subMatrix(bData, aData)
                print("The subtracted matrix B-A is: ")
                print(np.matrix(result))
            else:
                print("A and B must be the same size.")
        else:
            print("Matrix A or B does not exist, try loading it!")
    elif(inp == 17):
        if('aData' in globals()) and ('bData' in globals()):
            if(len(aData[0]) == len(bData[0])) and (len(aData) == len(bData)):
                result = subMatrix(aData, bData)
                print("The subtracted matrix A-B is: ")
                print(np.matrix(result))
            else:
                print("A and B must be the same size.")
        else:
            print("Matrix A or B does not exist, try loading it!")
    elif(inp == 18):
        if('aData' in globals()) and ('bData' in globals()):
            if(len(aData[0]) == len(bData)):
                result = matrixMult(aData, bData)
                print("A * B is: ")
                print(np.matrix(result))
            else:
                print("A's columns must equal B's rows!")
        else:
            print("Matrix A or B does not exist, try loading it!")
    elif(inp == 19):
        if('aData' in globals()) and ('bData' in globals()):
            if(len(bData[0]) == len(aData)):
                result = matrixMult(bData, aData)
                print("B * A is: ")
                print(np.matrix(result))
            else:
                print("B's columns must equal A's rows!")
        else:
            print("Matrix A or B does not exist, try loading it!")
    elif(inp == 20):
        if('aData' in globals()):
            copyAtoB()
            print("B: ")
            print(np.matrix(bData))
        else:
            print("A matrix does not exist! Cannot copy to B!")
    elif(inp == 21):
        if('bData' in globals()):
            copyBtoA()
            print("A: ")
            print(np.matrix(bData))
        else:
            print("B matrix does not exist! Cannot copy to A!")
    elif(inp == 22):
        if('aData' in globals()) and ('bData' in globals()):
            swapAandB()
        else:
            print("Either A or B does not exist!")
    elif(inp == 23):
        if('aData' in globals()):
            print("A matrix is: ")
            print(np.matrix(aData))
        else:
            print("Nothing in matrix A, try loading it!")
    elif(inp == 24):
        if('bData' in globals()):
            print("B matrix is: ")
            print(np.matrix(bData))
        else:
            print("Nothing in matrix B, try loading it!")


