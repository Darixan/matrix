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

def Determinate(matrix)

end

def Transpose(matrix)

end

def Inverse(matrix)

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

end

def Copy_AB()

end

def Copy_BA()

end

def Swap(matrix1, matrix2)

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
matrixA = []
matrixB = []
matrixC = []
while true
    Menu()
    choice = gets.chomp.to_i
    case choice
        when 0
            break
        
        when 1
            matrixA = LoadA()
            print matrixA
        
        when 2
            matrixB = LoadB()
            print matrixB
        
        when 5
            puts "Please enter a value for 'n': \n"
            inp = Integer(gets) rescue false
            while inp == false
                puts "Please enter an INTEGER for 'n': \n"
                inp = Integer(gets) rescue false
            end
            matrixC = constMult(matrixA, inp)
            print matrixC
            puts "\n"
            
            puts "Would you like to store the result of A? (Y/N)\n"
            inp = gets.chomp
            while inp != "Y" && inp != "N"
                puts "Please input 'Y' for yes, 'N' for no.\n"
                inp = gets.chomp
            end
            if inp == "Y"
                matrixA = matrixC
            end
        when 6
            puts "Please enter a value for 'n': \n"
            inp = Integer(gets) rescue false
            while inp == false
                puts "Please enter an INTEGER for 'n': \n"
                inp = Integer(gets) rescue false
            end
            matrixC = constMult(matrixB, inp)
            print matrixC
            puts "\n"
            
            puts "Would you like to store the result of B? (Y/N)\n"
            inp = gets.chomp
            while inp != "Y" && inp != "N"
                puts "Please input 'Y' for yes, 'N' for no.\n"
                inp = gets.chomp
            end
            if inp == "Y"
                matrixB = matrixC
            end
        
        when 13
            matrixC = addMatrix(matrixA, matrixB) 
            print matrixC
        
        when 14
            matrixC = subMatrix(matrixB, matrixA)
            print matrixC
        
        when 15
            matrixC = subMatrix(matrixA, matrixB)
            print matrixC
        
        when 21
            print matrixA
        
        when 22
            print matrixB
        
        else
            puts "INVALID INPUT"
    end
end
