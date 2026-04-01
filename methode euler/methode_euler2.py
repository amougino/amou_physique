
import matplotlib.pyplot as plt
import numpy as np

g = 9.81
rhob = 8e3
r = 1e-3

cx = 0.45
rhoa = 1.3

alpha = (3 * cx * rhoa) / (8 * r * rhob)
tau = 1/(2*np.sqrt(alpha*g))


def next_iter(dt, a, v_0):
    print(a*dt)
    v_1 = v_0 + a*dt
    return v_1


t = [0]
v = [0]

n = 100000
dt = 7*tau/n

for i in range(n):
    a = -alpha*(v[-1]**2) + g
    v.append(next_iter(dt, a, v[-1]))
    t.append(t[-1]+dt)

t_arr = np.array(t)
v_arr = np.array(v)

vf = np.sqrt(g)/np.sqrt(alpha)

fig1, ax1 = plt.subplots()
ax1.scatter(t_arr, v_arr, marker=".", c="r")
ax1.plot(t_arr, vf*np.tanh(t_arr/tau), c="b")

plt.show()
