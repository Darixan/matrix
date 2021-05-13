#!/usr/bin/ruby
###############################################################################
# Course: CMPS 3500
# Class Project
# RUBY IMPLEMENTATION OF A CUSTOM MATRIX CALCULATOR
# Date: 04/30/21
# Student 1: Paula Rodriguez
# Student 2: Adrian Jay Telan
# Student 3: Terry Watson
# Description: Implementation of a scientific calculator
###############################################################################
require 'csv'

#unary operations
def LoadA()
    file = CSV.parse(File.read("A.csv"), converters: :integer, headers: false)
end

def LoadB()
    file = CSV.parse(File.read("B.csv"), converters: :integer, headers: false)
end

###IDENTITY MATRIX HERE
def toIdentity(n)
    if n == 1
        return [1]
    end
    
    id = Array.new(n){Array.new(n)}

    i = 0
    j = 0

    id.each do |idRow|
        idRow.each do |idCol|
            if i == j
                id[i][j] = 1
            else
                id[i][j] = 0
            end
            j = j + 1
        end
        i = i + 1
        j = 0
    end
    return id

end

def toIdentityA(size)
    $matrixA = toIdentity(size)
end

def toIdentityB(size)
    $matrixB = toIdentity(size)
end

###SCALAR HERE 
def constMult(matrix, const)
    row = matrix[0].length
    col = matrix.length
    newMatrix = Array.new(col){Array.new(row)}

    i = 0
    j = 0

    matrix.each do |mRow|
        mRow.each do |mCol|
            newMatrix[i][j] = mCol * const
            j = j + 1
        end
        i = i + 1
        j = 0
    end
    return newMatrix

end

def cofactor(mat, i, j)
    n = []
    for row in mat[0,i]+mat[i+1, mat.length()] do
      n.push(row[0,j]+row[j+1,row.length()])
    end
    return n
end

def Determinant(matrix)
    if matrix.length == 2
        determinant = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return determinant
    end

    detSum = 0

    i = 0
    matrix[0].each do |mCol|
        sign = (-1) ** (i)

        subDet = Determinant(cofactor(matrix, 0, i))

        detSum = (sign * matrix[0][i] * subDet) + detSum
        i = i + 1
    end
    return detSum


end

def Transpose(matrix)
    row = matrix[0].length
    col = matrix.length
    transposedMatrix = Array.new(col){Array.new(row)}

    i = 0
    j = 0
    
    transposedMatrix.each do |tRow|
        tRow.each do |tCol|
            transposedMatrix[i][j] = matrix[j][i]
            j = j + 1
        end
        i = i + 1
        j = 0
    end
    return transposedMatrix
end

def Adjoint(matrix)
    adjoint = Array.new(matrix.length){Array.new(matrix.length)}
    if matrix.length == 1
        adjoint = [1]
        return adjoint
    end

    sign = 1

    matrix.each do |mRow|
        mRow.each do |mCol|
            if (i+j)%2 == 0
                sign = 1
            else
                sign = -1
            end
            adjoint[j][i] = sign * determinant(cofactor(matrix,i,j))
        end
    end
    return adjoint
end

def Inverse(matrix)
    determinant = Determinant(matrix)

    adjoint = Adjoint(matrix)
end

def Power()

end

#binary operations
def addMatrix(matrix1, matrix2)
    row = matrix1[0].length
    col = matrix1.length
    matrix3 = Array.new(col){Array.new(row)}
    
    i = 0
    j = 0

    matrix1.each do |m1Row|
        m1Row.each do |m1Col|
            matrix3[i][j] = m1Col + matrix2[i][j]
            j = j + 1
        end
        i = i + 1
        j = 0
    end

    return matrix3
end

def subMatrix(matrix1, matrix2)
    row = matrix1[0].length
    col = matrix1.length
    matrix3 = Array.new(col){Array.new(row)}
    
    i = 0
    j = 0

    matrix1.each do |m1Row|
        m1Row.each do |m1Col|
            matrix3[i][j] = m1Col - matrix2[i][j]
            j = j + 1
        end
        i = i + 1
        j = 0
    end

    return matrix3

end

def multMatrix(matrix1, matrix2)
    row = matrix1.length
    col = matrix2[0].length
    matrix3 = Array.new(col){Array.new(row, 0)}

    i = 0
    j = 0
    k = 0

    matrix1.each do |m1Row|
        m1Row.each do |m1Col|
            matrix2.each do |m2Row|
                matrix3[i][j] = (matrix1[i][k] * matrix2[k][j]) + matrix3[i][j]
                k = k + 1
            end
            j = j + 1
            k = 0
        end
        i = i + 1
        j = 0
    end
    
    return matrix3
end

def Copy_A_to_B()
    $matrixB = $matrixA
end

def Copy_B_to_A()
    $matrixA = $matrixB
end

def Swap()
    tmp = $matrixA
    $matrixA = $matrixB
    $matrixB = tmp
end

def Menu()
    puts "\n\nCHOOSE AN OPTION:"
    puts "**********************************"
    puts "1\tLoad Matrix A\n"
    puts "2\tLoad Matrix B\n"
    puts "3\tMake A a square identity matrix: A to I\n"
    puts "4\tMake B a square identity matrix: B to I\n"
    puts "5\tA times n (will be prompted for n)\n"
    puts "6\tB times n (will be prompted for n)\n"
    puts "7\tDeterminant of A\n"
    puts "8\tDeterminant of B\n"
    puts "9\tTranspose A\n"
    puts "10\tTranspose B\n"
    puts "11\tInverse of A\n"
    puts "12\tInverse of B\n"
    puts "13\tA + B\n"
    puts "14\tB - A\n"
    puts "15\tA - B\n"
    puts "16\tA * B\n"
    puts "17\tB * A\n"
    puts "18\tB = A\n"
    puts "19\tA = B\n"
    puts "20\tSwap A and B\n"
    puts "21\tPrint A\n"
    puts "22\tPrint B\n"
    puts "0\tQuit\n\n"
end

#MAIN STARTS HERE
$matrixA = []
$matrixB = []
$matrixC = []
while true
    Menu()
    choice = gets.chomp.to_i
    case choice
        when 0
            break
        
        when 1
            $matrixA = LoadA()
            width = $matrixA.flatten.max.to_s.size+2
            puts $matrixA.map {|a| a.map {|i| i.to_s.rjust(width)}.join}
        
        when 2
            $matrixB = LoadB()
            width = $matrixB.flatten.max.to_s.size+2
            puts $matrixB.map {|a| a.map {|i| i.to_s.rjust(width)}.join}

        when 3
            matrixA = $matrixA
            row = matrixA[0].length
            col = matrixA.length
            if row == col
                toIdentityA(col)
                puts "A is now: \n"
                width = $matrixA.flatten.max.to_s.size+2
                puts $matrixA.map {|a| a.map {|i| i.to_s.rjust(width)}.join}
            else
                puts "A is not a square matrix\n"
            end

        when 4
            matrixB = $matrixB
            row = matrixB[0].length
            col = matrixB.length
            if row == col
                toIdentityB(col)
                puts "B is now: \n"
                width = $matrixB.flatten.max.to_s.size+2
                puts $matrixB.map {|a| a.map {|i| i.to_s.rjust(width)}.join}
            else
                puts "B is not a square matrix\n"
            end

        when 5
            puts "Please enter a value for 'n': \n"
            inp = Integer(gets) rescue false
            while inp == false
                puts "Please enter an INTEGER for 'n': \n"
                inp = Integer(gets) rescue false
            end
            $matrixC = constMult($matrixA, inp)
            width = $matrixC.flatten.max.to_s.size+2
            puts $matrixC.map {|a| a.map {|i| i.to_s.rjust(width)}.join}
            puts "\n"
            
            puts "Would you like to store the result of A? (Y/N)\n"
            inp = gets.chomp
            while inp != "Y" && inp != "N"
                puts "Please input 'Y' for yes, 'N' for no.\n"
                inp = gets.chomp
            end
            if inp == "Y"
                $matrixA = $matrixC
            end
        when 6
            puts "Please enter a value for 'n': \n"
            inp = Integer(gets) rescue false
            while inp == false
                puts "Please enter an INTEGER for 'n': \n"
                inp = Integer(gets) rescue false
            end
            $matrixC = constMult($matrixB, inp)
            width = $matrixC.flatten.max.to_s.size+2
            puts $matrixC.map {|a| a.map {|i| i.to_s.rjust(width)}.join}
            puts "\n"
            
            puts "Would you like to store the result of B? (Y/N)\n"
            inp = gets.chomp
            while inp != "Y" && inp != "N"
                puts "Please input 'Y' for yes, 'N' for no.\n"
                inp = gets.chomp
            end
            if inp == "Y"
                $matrixB = $matrixC
            end

        when 7
            if $matrixA[0].length == $matrixA.length
                determinant = Determinant($matrixA)
                puts "The determinant is: \n"
                print determinant
                puts "\n"
            else
                puts "Matrix A must be a square matrix\n"
            end 
       
        when 8
            if $matrixB[0].length == $matrixB.length
                determinant = Determinant($matrixB)
                puts "The determinant is: \n"
                print determinant
                puts "\n"
            else
                puts "Matrix B must be a square matrix\n"
            end 
        
        when 9
            $matrixC = Transpose($matrixA)
            puts "Transposed matrix: \n"
            width = $matrixC.flatten.max.to_s.size+2
            puts $matrixC.map {|a| a.map {|i| i.to_s.rjust(width)}.join}
        
        when 10
            $matrixC = Transpose($matrixB)
            puts "Transposed matrix: \n"
            width = $matrixC.flatten.max.to_s.size+2
            puts $matrixC.map {|a| a.map {|i| i.to_s.rjust(width)}.join}

        when 11
            if $matrixA[0].length == $matrixA.length
                $matrixC = Inverse($matrixA)
                puts "The inverse matrix for Matrix A is: \n"
                width = $matrixC.flatten.max.to_s.size+2
                puts $matrixC.map {|a| a.map {|i| i.to_s.rjust(width)}.join}
                puts "\n" 
            else
                puts "Matrix A must be a square matrix\n"
            end

        when 13
            $matrixC = addMatrix($matrixA, $matrixB) 
            width = $matrixC.flatten.max.to_s.size+2
            puts $matrixC.map {|a| a.map {|i| i.to_s.rjust(width)}.join}
        
        when 14
            $matrixC = subMatrix($matrixB, $matrixA)
            width = $matrixC.flatten.max.to_s.size+2
            puts $matrixC.map {|a| a.map {|i| i.to_s.rjust(width)}.join}
        
        when 15
            $matrixC = subMatrix($matrixA, $matrixB)
            width = $matrixC.flatten.max.to_s.size+2
            puts $matrixC.map {|a| a.map {|i| i.to_s.rjust(width)}.join}

        when 16
            if $matrixA[0].length == $matrixB.length
                puts "A * B is: \n"
                $matrixC = multMatrix($matrixA, $matrixB)
                width = $matrixC.flatten.max.to_s.size+2
                puts $matrixC.map {|a| a.map {|i| i.to_s.rjust(width)}.join}
            else
                puts "Matrix A's column length must equal B's row length\n"
            end
        when 17
            if $matrixB[0].length == $matrixA.length
                puts "A * B is: \n"
                $matrixC = multMatrix($matrixB, $matrixA)
                width = $matrixC.flatten.max.to_s.size+2
                puts $matrixC.map {|a| a.map {|i| i.to_s.rjust(width)}.join}
            else
                puts "Matrix B's column length must equal A's row length\n"
            end

        when 18
            Copy_A_to_B()
            puts "Matrix A: \n"
            width = $matrixA.flatten.max.to_s.size+2
            puts $matrixA.map {|a| a.map {|i| i.to_s.rjust(width)}.join}
            puts "\n"
            puts "Matrix B: \n"
            width = $matrixB.flatten.max.to_s.size+2
            puts $matrixB.map {|a| a.map {|i| i.to_s.rjust(width)}.join}
            puts "\n"

        when 19
            Copy_B_to_A()
            puts "Matrix A: \n"
            width = $matrixA.flatten.max.to_s.size+2
            puts $matrixA.map {|a| a.map {|i| i.to_s.rjust(width)}.join}
            puts "\n"
            puts "Matrix B: \n"
            width = $matrixB.flatten.max.to_s.size+2
            puts $matrixB.map {|a| a.map {|i| i.to_s.rjust(width)}.join}
            puts "\n"

        when 20
            Swap()
            puts "Matrix A: \n"
            width = $matrixA.flatten.max.to_s.size+2
            puts $matrixA.map {|a| a.map {|i| i.to_s.rjust(width)}.join}
            puts "\n"
            puts "Matrix B: \n"
            width = $matrixB.flatten.max.to_s.size+2
            puts $matrixB.map {|a| a.map {|i| i.to_s.rjust(width)}.join}
            puts "\n" 
            
        when 21
            puts "Matrix A: \n"
            width = $matrixA.flatten.max.to_s.size+2
            puts $matrixA.map {|a| a.map {|i| i.to_s.rjust(width)}.join}
            puts "\n"
        when 22
            puts "Matrix B: \n"
            width = $matrixB.flatten.max.to_s.size+2
            puts $matrixB.map {|a| a.map {|i| i.to_s.rjust(width)}.join}
            puts "\n"

        else
            puts "INVALID INPUT"
    end
end
