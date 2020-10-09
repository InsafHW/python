N = int(input())

def outText(N):
	if (N < 10):
		out = 0
		for i in range(N):
			out += i
	elif (N >= 10 and N < 20):
		out = 'used numbers='
		for i in range(N):
			if (i == N - 1):
				out = out + str(i)
			else:
				out = out + str(i) + ', '
	else:
		out = "very big number"

	return out

print(outText(N))