string = input() #3, 4, 3.0
def count(string):
	numArr = string.split(', ')
	num1 = bin(round(float(numArr[0])))
	num2 = bin(round(float(numArr[1])))
	num3 = bin(round(float(numArr[2])))

	countOne = 0
	countTwo = 0
	countThree = 0

	for i in str(num1):
		if i == '1':
			countOne += 1
	for i in str(num2):
		if i == '1':
			countTwo += 1
	for i in str(num3):
		if i == '1':
			countThree += 1


	if (countOne > countTwo):
		countOne, countTwo = countTwo, countOne
	if (countTwo > countThree):
		countTwo, countThree = countThree, countTwo
	if (countOne > countTwo):
		countOne, countTwo = countTwo, countOne

	outStr = str(countOne) + ', ' + str(countTwo) + ', ' + str(countThree)
	return outStr



print(count(string))