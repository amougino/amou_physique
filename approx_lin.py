import numpy as np

x1 = [40, 50, 100, 120, 280, 400]
y1 = [16, 13.5, 8.5, 6, 3, 1.8]


def tot(x, y, coef):
    sum = 0
    for i in range(len(x)):
        sum += (((x[i] - x[0])*coef + y[0]) - y[i])**2
    sqrt = np.sqrt(sum)
    # print("S", sqrt)
    return sqrt


def find(x, y, value, steps):
    step = 0.1
    direction = 1
    previous = value
    for i in range(steps):
        if tot(x, y, previous) < tot(x, y, value):
            # print('flip', previous, value)
            direction *= -1
            step /= 2
            previous = value
            value += step*direction
        else:
            previous = value
            value += step*direction
        # print(value)
    return value


print(find(x1, y1, -0.5, 40))
