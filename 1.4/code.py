def form_list(N, K):
	if N > 50 or K > 10 or N < 1 or K < 1:
		return "Error"

	res = []
	if N % K == 0:
		for i in range(1, N + 1):
			res.append(i)
	else:
		currentPerson = K;
		ostavList = list(range(1, N + 1)) # список оставшихся людей
		while (len(ostavList) != 1 or len(ostavList) >= K):
			res.append(currentPerson)
			ostavList.remove(currentPerson)

			if currentPerson <= N - K:
				currentPerson += K
			else:
				difference = len(ostavList) - currentPerson
				currentPerson = ostavList[0] + difference
	return res

N = int(input()) #кол-во человек
K = int(input()) #каждый k выбывает

print(form_list(N, K))
