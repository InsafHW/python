string = input()

def check(string):
	countCols = 0
	for i in string:
		if (i == ','):
			countCols += 1
	newArr = string.split(',')
	hasMarital = True
	fullName = newArr[0]
	sex = newArr[1]
	univGroup = newArr[2]
	marital = newArr[3]
	height = int(newArr[4])
	physGroup = newArr[5]

	if (marital != ''):
		hasMarital = True
	else:
		hasMarital = False
		
	isValidHeight = False
	isValidPhysGroup = False
	if (sex == 'муж'):
		if (height >= 180):
			isValidHeight = True
	elif (sex == 'жен'):
		if (height >= 175):
			isValidHeight = True
	
	if (physGroup == 'спорт' or physGroup == 'общая'):
		isValidPhysGroup = True

	if (isValidHeight and isValidPhysGroup):
		if (hasMarital):
			outStr = fullName + ',' + str(height) + ',' + marital
		else:
			outStr = fullName + ',' + str(height) + ',' + 'пропуск'

	else:
		if (hasMarital):
			outStr = fullName + ',' + 'не подходит' + ',' + marital
		else:
			outStr = fullName + ',' + 'не подходит' + ',' + 'пропуск'

	return outStr

print(check(string))