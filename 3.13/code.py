def form_list(N, K):
	res = []
	people = list(range(1, N + 1)) #[1, 2, 3...., 12]
	index = K - 1
	while len(res) != N:
		res.append(people[index])
		people.remove(people[index])
		
		index += K - 1
		while (index >= len(people)):
			index = index - len(people)
			if (len(people) == 0):
				break
	return res

#N = int(input()) #9
#K = int(input()) #8

print(form_list(7, 2))