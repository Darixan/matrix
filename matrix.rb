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

end

def subMatrix(matrix1, matrix2)

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
    puts "1\tLoad Matrix A\n2\tLoad Matrix B\n0\tQuit\n\n"
end

#MAIN STARTS HERE
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
        else
            puts "INVALID INPUT"
    end
end
