# def form_list(N, K):
# 	res = []
# 	totalPersons = list(range(1,N + 1))
# 	currentPerson = K
# 	while (len(totalPersons) != 1 or len(totalPersons) >= K):
# 		res.append(currentPerson)
# 		totalPersons.remove(currentPerson)
# 		if (currentPerson < len(totalPersons) - K):
# 			currentPerson += K
# 			while (currentPerson in totalPersons):
# 				currentPerson += 1
			
# 		else:
# 			currentPerson = totalPersons[0]

# 	return res

# N = int(input()) #кол-во человек
# K = int(input()) #каждый k выбывает

# print(form_list(N, K))

def form_list(N, K):
	res = []
	totalPersons = list(range(1,N + 1))
	currentPerson = K
	while (len(totalPersons) != 1 or len(totalPersons) >= K):
		res.append(currentPerson)
		totalPersons.remove(currentPerson)
		if currentPerson <= N - K:
			currentPerson += K
			while (currentPerson in totalPersons):
				currentPerson += K
		else:
			currentPerson = totalPersons[0]
	return res

N = int(input()) #кол-во человек
K = int(input()) #каждый k выбывает

print(form_list(N, K))
