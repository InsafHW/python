import numpy as np

battle_state = np.array(
   [[0,0,0,0], 
   [0,-1,2,0], 
   [0,0,-1,0], 
   [0,2,0,1]])


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

	positionState.append(last_move[1] - 1) #Потому что индексация с 0

	available_moves = np.full((4,4), True)
	
	for i in range(battle_state.shape[0]):
		for j in range(battle_state.shape[1]):
			#УБрать, позицию куда промахивались 
			if battle_state[i][j] < 0:
				available_moves[i][j] = False
			if battle_state[i][j] == 2:
				available_moves[i][j] = False
				#Убрать ход справа
				if (i + 1 <= 3):
					available_moves[i + 1][j] = False
				#Убрать ход слева
				if (i - 1 >= 0):
					available_moves[i - 1][j] = False
				#Убрать ход сверху
				if (j + 1 <= 3):
					available_moves[i][j + 1] = False
				#Убрать ход снизу
				if (j - 1 >= 0):
					available_moves[i][j - 1] = False
	
	step = []
	#Доступно стрелять вправо
	if (positionState[0] + 1 <= 3):
		if (battle_state[positionState[1]][positionState[0] + 1] >= 0 and available_moves[positionState[1]][positionState[0] + 1] == True):
			step.append([positionState[0] + 1, positionState[1]])
	#Доступно стрелять влево
	if (positionState[0] - 1 >= 0):
		if (battle_state[positionState[1]][positionState[0] - 1] >= 0 and available_moves[positionState[1]][positionState[0] - 1] == True):
			step.append([positionState[0] - 1, positionState[1]])
	#Доступно стрелять вниз
	if (positionState[1] + 1 <= 3):
		if (battle_state[positionState[1] + 1][positionState[0]] >= 0 and available_moves[positionState[1] + 1][positionState[0]] == True):
			step.append([positionState[0], positionState[1] + 1])
	#Доступно стрелять вверх
	if (positionState[1] - 1 >= 0):
		if (battle_state[positionState[1] - 1][positionState[0]] >= 0 and available_moves[positionState[1] - 1][positionState[0]] == True):
			step.append([positionState[0], positionState[1] - 1])
	

	if step[0][0] == 0:
		x = 'a'
	elif step[0][0] == 1:
		x = 'b'
	elif step[0][0] == 2:
		x = 'c'
	elif step[0][0] == 3:
		x = 'd'
	
	move = (x, step[0][1] + 1)
	return move


print(kill_boat(battle_state, ('d', 4)))