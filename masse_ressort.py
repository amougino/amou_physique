import numpy as np
from sklearn.linear_model import LinearRegression
g = 9.81
P = np.array([0.02, 0.05, 0.1, 0.15, 0.2, 0.25])*g
dl = np.array([0.01, 0.027, 0.058, 0.085, 0.115, 0.143]).reshape((-1, 1))
print(dl)
reg = LinearRegression().fit(dl, P)
print(reg.score(dl, P))
