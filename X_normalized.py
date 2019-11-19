import numpy as np

X=np.random.random((5,5))
Y = (X-X.mean()) / X.std()
print(Y)