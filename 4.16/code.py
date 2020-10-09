import numpy as np
import random

battle_state = np.array([[1,0,0,2], 
	[0,-1,-1,0],
	[0,0,0,0],
	[0,2,0,2]])

def choose_act(battle_state, last_move, result):
	#move = (letter, number)

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
	#print(available_moves)
	positionState = []
	if result == "injury":
		print('last move', last_move)
		if last_move[0] == 'a':
			positionState.append(0)
		elif last_move[0] == 'b':
			positionState.append(1)
		elif last_move[0] == 'c':
			positionState.append(2)
		elif last_move[0] == 'd':
			positionState.append(3)
		positionState.append(last_move[1] - 1)
	#print(positionState)
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
				#if (available_moves[i][j] == )
				if (available_moves[i][j]) == True:
					step.append((j, i))
				
	#Сделать ход для injury
	
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
	#print(move)
	return move

print(choose_act(battle_state, ('a', 1), 'injury'))