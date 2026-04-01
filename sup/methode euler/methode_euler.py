import matplotlib.pyplot as plt
import numpy as np

eta = 1.8e-5
rhob = 8e3
r = 1e-3
g = 9.81

tau = (9 * (r**2) * rhob) / (2 * eta)
dt = 1e-3*tau


def next_iter(dt, a, v_0):
    print(a*dt)
    v_1 = v_0 + a*dt
    return v_1


t = [0]
v = [0]

max_t = 7*tau
while t[-1] < max_t:
    a = -(v[-1]/tau) + g
    v.append(next_iter(dt, a, v[-1]))
    t.append(t[-1]+dt)

t_arr = np.array(t)
v_arr = np.array(v)
fig1, ax1 = plt.subplots()
ax1.scatter(t_arr/tau, np.log(v_arr/(g*tau)), marker=".", c="r")

plt.show()
