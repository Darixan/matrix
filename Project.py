"""

"""
import csv
import numpy as np
def loadA():
	file = 'A.csv'
	with open(file, newline = '') as csvfile:
		data = []
		csv_reader = csv.reader(csvfile, delimiter = ',')
		for row in csv_reader:
			data.append(row)
		return data
	
def loadB():
	file = 'B.csv'
	with open(file, newline = '') as csvfile:
		data = []
		csv_reader = csv.reader(csvfile, delimiter = ',')
		for row in csv_reader:
			data.append(row)
		return data
	
aData = loadA()
bData = loadB()

print(np.matrix(aData))
print(np.matrix(bData))