import random
import numpy as np

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

def start_boats_position(how_many_boats):
	n1 = how_many_boats[0] # кол-во однопалубных
	n2 = how_many_boats[1] # кол-во двухпалубных
        
	boats_position = []
	available_x = ('a', 'b', 'c', 'd')
	available_y = (1, 2, 3, 4)
	available_positions = []
	for i in available_x:
		for j in available_y:
			position = (i, j)
			available_positions.append(position)
   

	for i in range(1, n1 + 1):
		pos = available_positions[random.randint(0, len(available_positions) - 1)]
		boats_position.append([pos])
		available_positions.remove(pos)
		delete_close_positions(pos[0], pos[1], available_x, available_y, available_positions)
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
				delete_close_positions(x2, y2, available_x, available_y, available_positions)
		elif (available_x.index(x1) -1 >= 0) and ((available_x[available_x.index(x1) - 1], y1) in available_positions):
			#Доступен выбор длины по x налево
			if (available_x[available_x.index(x1) - 1] in available_x):
				isEndFind = True
				y2 = y1
				x2 = available_x[available_x.index(x1) - 1]
				delete_close_positions(x2, y2, available_x, available_y, available_positions)
		elif (available_y.index(y1) + 1 <= len(available_y) - 1) and ((x1, available_y[available_y.index(y1) + 1]) in available_positions) and not isEndFind:
			#Доступен выбор длины по y вниз
			if (available_y[available_y.index(y1) + 1] in available_y):
				isEndFind = True
				x2 = x1
				y2 = available_y[available_y.index(y1) + 1]
				delete_close_positions(x2, y2, available_x, available_y, available_positions)
		elif (available_y.index(y1) - 1 > 0) and (x1, available_y[available_y.index(y1) - 1] in available_positions) and not isEndFind:
			#Доступен выбор длины по y вверх
			if (available_y[available_y.index(y1) - 1] in available_y):
				isEndFind = True
				x2 = x1
				y2 = available_y[available_y.index(y1) - 1]
				delete_close_positions(x2, y2, available_x, available_y, available_positions)
		else:
			print(available_positions);
			print("There is no available positions")
			print("startPos: ", startPos)
			return
		
		#Убрать близлежащие точки к (x1, y1), (x2, y2)
		delete_close_positions(x1, y1, available_x, available_y, available_positions)
		delete_close_positions(x2, y2, available_x, available_y, available_positions)
		boats_position.append([(x1, y1), (x2, y2)])
		
	
	return boats_position    

def choose_act(battle_state, last_move, result):
	available_moves = np.full((4,4), True)

	for i in range(battle_state.shape[0]):
		for j in range(battle_state.shape[1]):
			if battle_state[i][j] < 0:
				available_moves[i][j] = False
			if battle_state[i][j] == 1:
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
	
	positionState = []
	if result == "injury":
		if last_move[0] == 'a':
			positionState.append(0)
		elif last_move[0] == 'b':
			positionState.append(1)
		elif last_move[0] == 'c':
			positionState.append(2)
		elif last_move[0] == 'd':
			positionState.append(3)
		positionState.append(last_move[1] - 1)
	
	if len(positionState):
		if (positionState[0] + 1 <= 3):
			if (available_moves[positionState[1]][positionState[0] + 1] == True):
				step.append([positionState[0] + 1, positionState[1]])
		if (positionState[0] - 1 >= 0):
			if (available_moves[positionState[1]][positionState[0] - 1] == True):
				step.append([positionState[0] - 1, positionState[1]])
		if (positionState[1] + 1 <= 3):
			if (available_moves[positionState[1] + 1][positionState[0]] == True):
				step.append([positionState[0], positionState[1] + 1])
		if (positionState[1] - 1 >= 0):
			if (available_moves[positionState[1] - 1][positionState[0]] == True):
				step.append([positionState[0], positionState[1] - 1])
	else:
		for i in range(available_moves.shape[0]):
			for j in range(available_moves.shape[1]):
				if (available_moves[i][j]) == True:
					step.append((j, i))
				
	
	randomChoice = random.randint(0, len(step) - 1)
	
	if step[randomChoice][0] == 0:
		x = 'a'
	elif step[randomChoice][0] == 1:
		x = 'b'
	elif step[randomChoice][0] == 2:
		x = 'c'
	elif step[randomChoice][0] == 3:
		x = 'd'

	move = (x, step[randomChoice][1] + 1)
	return move
