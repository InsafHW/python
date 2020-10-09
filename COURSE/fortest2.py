x = 2
def g(x):
    x = x + 5
    def h(y):
    	return x + y
    return h(-1)
print(g(x))