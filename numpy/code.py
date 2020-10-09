import numpy as np

def recalcXC(xtab): 
	zeroClasterX = []
	zeroClasterY = []
	oneClasterX = []
	oneClasterY = []
	
	for i in range(xtab.shape[0]):
		if xtab[i][2] == 0:
			zeroClasterX.append(xtab[i][0])
			zeroClasterY.append(xtab[i][1])
		elif xtab[i][2] == 1:
			oneClasterX.append(xtab[i][0])
			oneClasterY.append(xtab[i][1])

	aveZeroClassterX = 0
	aveZeroClassterY = 0
	aveOneClassterX = 0
	aveOneClassterY = 0

	for i in range(len(zeroClasterX)):
		aveZeroClassterX = aveZeroClassterX + zeroClasterX[i]

	for i in range(len(zeroClasterY)):
		aveZeroClassterY = aveZeroClassterY + zeroClasterY[i]

	for i in range(len(oneClasterX)):
		aveOneClassterX = aveOneClassterX + oneClasterX[i]

	for i in range(len(oneClasterY)):
		aveOneClassterY = aveOneClassterY + oneClasterY[i]

	aveZeroClassterX = aveZeroClassterX / len(zeroClasterX)
	aveZeroClassterY = aveZeroClassterY / len(zeroClasterY)
	aveOneClassterX = aveOneClassterX / len(oneClasterX)
	aveOneClassterY = aveOneClassterY / len(oneClasterY)

	xctab = np.array([[aveZeroClassterX, aveZeroClassterY], [aveOneClassterX, aveOneClassterY]])

	return xctab

print(recalcXC(xtab))