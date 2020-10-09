import random

def start_boats_position(how_many_boats):
	boats_position = []
	available_x = ('a', 'b', 'c', 'd')
	available_y = (1, 2, 3, 4)
	available_positions = []
	for i in available_x:
		for j in available_y:
			position = (i, j)
			available_positions.append(position)
	n1, n2 = how_many_boats

	for i in range(1, n1 + 1):
		pos = available_positions[random.randint(0, len(available_positions) - 1)]
		boats_position.append(pos)
		available_positions.remove(pos)
		
	for i in range(1, n2 + 1):
		startPos = available_positions[random.randint(0, len(available_positions) - 1)]
		x1 = startPos[0]
		y1 = startPos[1]
		available_positions.remove(startPos)

		isEndFind = False

		if (available_x.index(x1) + 1 <= len(available_x) - 1) and ((available_x[available_x.index(x1) + 1], y1) in available_positions) and not isEndFind:
			#Доступен выбор длины по x направо
			if (available_x[available_x.index(x1) + 1] in available_x):
				isEndFind = True
				y2 = y1
				x2 = available_x[available_x.index(x1) + 1]
		elif (available_x.index(x1) -1 >= 0) and ((available_x[available_x.index(x1) - 1], y1) in available_positions):
			#Доступен выбор длины по x налево
			if (available_x[available_x.index(x1) - 1] in available_x):
				isEndFind = True
				y2 = y1
				x2 = available_x[available_x.index(x1) - 1]
		elif (available_y.index(y1) + 1 <= len(available_y) - 1) and ((x1, available_y[available_y.index(y1) + 1]) in available_positions) and not isEndFind:
			#Доступен выбор длины по y вниз
			if (available_y[available_y.index(y1) + 1] in available_y):
				isEndFind = True
				x2 = x1
				y2 = available_y[available_y.index(y1) + 1]
		elif (available_y.index(y1) - 1 > 0) and (x1, available_y[available_y.index(y1) - 1] in available_positions) and not isEndFind:
			#Доступен выбор длины по y вверх
			if (available_y[available_y.index(y1) - 1] in available_y):
				isEndFind = True
				x2 = x1
				y2 = available_y[available_y.index(y1) - 1]
		else:
			print(available_positions);
			print("There is no available positions")
			print("startPos: ", startPos)
			return
		
		boats_position.append([(x1, y1), (x2, y2)])
		available_positions.remove((x2, y2))
	

	return boats_position
	

print(start_boats_position((1, 1)))
