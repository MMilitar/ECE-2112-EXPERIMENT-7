import numpy as np

n = (np.linspace(1,100,100)**2)
N = n.reshape((10,10))
X = N%3 == 0
Y = N[N%3==0]

print(X)
print(Y)