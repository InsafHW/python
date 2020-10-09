import numpy as np

image = np.array([[1, 0, 2, 3],[4,6,6,8], [3,1,1,0], [1,2,2,4,]])
mask = np.array([1,-1,-1,1])

def maxpooling_2x2(image, mask):
	M, N = image.shape
	K = 2
	L = 2

	MK = M // K
	NL = N // L
	

	Q1 = image[:MK * K, :NL * L].reshape(MK, K, NL, L).max(axis=(1, 3))
	Q2 = image[MK * K:, :NL * L].reshape(-1, NL, L).max(axis=2)
	Q3 = image[:MK * K, NL * L:].reshape(MK, K, -1).max(axis=1)
	Q4 = image[MK * K:, NL * L:].max()

	soln = np.vstack([np.c_[Q1, Q3], np.c_[Q2, Q4]])

	left_top_quorte = image[:int(image.shape[0] / 2), :int(image.shape[1] / 2)]
	right_top_quorte = image[:int(image.shape[0] / 2), int(image.shape[1] / 2):]
	left_bottom_quorte = image[int(image.shape[0] / 2):, :int(image.shape[1] / 2)]
	right_bottom_quorte = image[int(image.shape[0] / 2):, int(image.shape[1] / 2):]

	left_top_max = np.amax(left_top_quorte)
	right_top_max = np.amax(right_top_quorte)
	left_bottom_max = np.amax(left_bottom_quorte)
	right_bottom_max = np.amax(right_bottom_quorte)

	res = np.array([[left_top_max, right_top_max], [left_bottom_max, right_bottom_max]])
	res = res.flatten()

	print(soln)
	

maxpooling_2x2(image, mask)