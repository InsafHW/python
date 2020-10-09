def delete_close_positions(x1, y1, available_x, available_y, available_positions):
	#Убрать правую точку
		if (available_x.index(x1) + 1 <= len(available_x) - 1):
			if (available_x[available_x.index(x1) + 1], y1) in available_positions:
				available_positions.remove((available_x[available_x.index(x1) + 1], y1))
				
		#Убрать левую точку
		if (available_x.index(x1) - 1) >= 0:
			if (available_x[available_x.index(x1) - 1], y1) in available_positions:
				available_positions.remove((available_x[available_x.index(x1) - 1], y1))
			
		#Убрать верхнюю точку
		if (available_y.index(y1) + 1) <= len(available_y) - 1:
			if (x1, available_y[available_y.index(y1) + 1]) in available_positions:
				available_positions.remove((x1, available_y[available_y.index(y1) + 1]))
		
		#Убрать нижнюю точку
		if (available_y.index(y1) - 1) >= 0:
			if (x1, available_y[available_y.index(y1) - 1]) in available_positions:
				available_positions.remove((x1, available_y[available_y.index(y1) - 1]))


def check(move, boats_position, shoots_map):
	#Создать доступные места
	#Убрать занятые из доступных
	available_x = ('a', 'b', 'c', 'd')
	available_y = (1, 2, 3, 4)
	available_positions = []
	for i in available_x:
		for j in available_y:
			position = (i, j)
			available_positions.append(position)

	for position in boats_position:
		if (len(position) == 2):
			delete_close_positions(position[0][0], position[0][1], available_x, available_y, available_positions)
			if (position[0][0] in available_positions):
				available_positions.remove(position[0][0])
			if (position[0][1] in available_positions):
				available_positions.remove(position[0][1])

			delete_close_positions(position[1][0], position[1][1], available_x, available_y, available_positions)
			if (position[1][0] in available_positions):
				available_positions.remove(position[1][0])
			if (position[1][1] in available_positions):
				available_positions.remove(position[1][1])

		elif (len(position) == 1):
			delete_close_positions(position[0][0], position[0][1], available_x, available_y, available_positions)
			if (position[0] in available_positions):
				available_positions.remove(position[0])
	
	res = 'miss'
	#Избавляемся от внешних []
	newBoats_position = list()
	for pos in boats_position:
		if (len(pos) == 1):
			newBoats_position.append(pos[0])
		if (len(pos) == 2):
			newBoats_position.append(pos[0])
			newBoats_position.append(pos[1])

	#Если данный ход уже был, увеличиваем кол-во
	if move in shoots_map:
		shoots_map[move] = shoots_map[move] + 1

	#Если хода не было, то добавляем его в историю
	else:
		shoots_map[move] = 1
		if (move in newBoats_position):	
			isInjured = False
			#Доступен вправо
			if (available_x.index(move[0]) + 1) <= len(available_x) - 1:
				if (available_x[available_x.index(move[0]) + 1], move[1]) in newBoats_position:
					isInjured = True
					res = "injury"
			#Доступен влево
			if (available_x.index(move[0]) - 1) >= 0:
				if (available_x[available_x.index(move[0]) - 1], move[1]) in newBoats_position:
					isInjured = True
					res = "injury"
			#Доступен вверх
			if (available_y.index(move[1]) + 1) <= len(available_y) - 1:
				if (move[0], available_y[available_y.index(move[1]) + 1]) in newBoats_position:
					isInjured = True
					res = "injury"
			#Доступен вниз
			if (available_y.index(move[1]) - 1) >= 0:
				if (move[0], available_y[available_y.index(move[1]) - 1]) in newBoats_position:
					isInjured = True
					res = "injury" 
			if not isInjured:
				res = "killed"

	return res

