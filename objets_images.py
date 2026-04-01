import matplotlib.pyplot as plt
import numpy as np


OA = [-125, -150, -200, -250, -300, -400]
OAp = [410, 270, 195, 165, 150, 130]
ApBp = [-62, -35, -19, -13, -10, -6]
AB = 20

OA_inv = []
OAp_inv = []
for i in range(6):
    OA_inv.append(1/OA[i])
    OAp_inv.append(1/OAp[i])

fig, ax = plt.subplots()
plt.plot(OA_inv, OAp_inv)
# plt.show()


def tot(x, y, coef):
    sum = 0
    for i in range(len(x)):
        sum += (((x[i] - x[0])*coef + y[0]) - y[i])**2
    sqrt = np.sqrt(sum)
    print("S", sqrt)
    return sqrt


def find(x, y, value, steps):
    step = 0.1
    direction = 1
    previous = value
    for i in range(steps):
        if tot(x, y, previous) < tot(x, y, value):
            print('flip', previous, value)
            direction *= -1
            step /= 2
            previous = value
            value += step*direction
        else:
            previous = value
            value += step*direction
        print(value)
    return value


coef = find(OA_inv, OAp_inv, 2, 100)
L = 0.01
plt.plot([OA_inv[0], 1*L + OA_inv[0]], [OAp_inv[0], coef*L + OAp_inv[0]])
plt.show()
