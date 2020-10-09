''' --------- модуль слушателя курса -------- '''

# функция выбора хода - добить двухпалубный корабль
def kill_boat(battle_state, last_move):
	positionState = []
	if last_move[0] == 'a':
		positionState.append(0)
	elif last_move[0] == 'b':
		positionState.append(1)
	elif last_move[0] == 'c':
		positionState.append(2)
	elif last_move[0] == 'd':
		positionState.append(3)

	positionState.append(last_move[1] - 1)

	#Доступно стрелять вправо
	if (positionState[0] + 1 < 4):
		if (battle_state[positionState[0] + 1][positionState[1]] >= 0 and battle_state[positionState[0] + 1][positionState[1]] != 1):
			step = (positionState[0] + 1, positionState[1])
	#Доступно стрелять влево
	elif (positionState[0] - 1 >= 0):
		if (battle_state[positionState[0] -1][positionState[1]] >= 0 and battle_state[positionState[0] - 1][positionState[1]] != 1):
			step = (positionState[0] - 1, positionState[1])
	#Доступно стрелять вверх
	elif (positionState[1] + 1 < 4):
		if (battle_state[positionState[0]][positionState[1] + 1] >= 0 and battle_state[positionState[0]][positionState[1] + 1] != 1):
			step = (positionState[0], positionState[1] + 1)
	#Доступно стрелять вниз
	elif (positionState[1] - 1 >= 0):
		if (battle_state[positionState[0]][positionState[1] - 1] >= 0 and battle_state[positionState[0]][positionState[1] - 1] != 1):
			step = (positionState[0], positionState[1] - 1)

	if step[0] == 0:
		x = 'a'
	elif step[0] == 1:
		x = 'b'
	elif step[0] == 2:
		x = 'c'
	elif step[0] ==3:
		x = 'd'
	
	move = (x, step[1] + 1)
	return move