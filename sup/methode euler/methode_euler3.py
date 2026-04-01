import matplotlib.pyplot as plt
import numpy as np

eta = 1.8e-5
rhob = 8e3
r = 1e-3
g = 9.81
cx = 0.45
rhoa = 1.3

alpha = (3 * cx * rhoa) / (8 * r * rhob)
tau1 = (9 * (r**2) * rhob) / (2 * eta)
tau2 = 1/(2*np.sqrt(alpha*g))
dt = 1e-3*tau1


def next_iter(dt, a, v_0):
    v_1 = v_0 + a*dt
    return v_1


t1 = [0]
v1 = [0]
t2 = [0]
v2 = [0]

vf1 = g*tau1
vf2 = np.sqrt(g)/np.sqrt(alpha)

n = 1000
dt = 7*tau2/n
max_t = 7*tau1

while t1[-1] < max_t:
    a = -(v1[-1]/tau1) + g
    v1.append(next_iter(dt, a, v1[-1]))
    t1.append(t1[-1]+dt)

for i in range(n):
    a = -alpha*(v2[-1]**2) + g
    v2.append(next_iter(dt, a, v2[-1]))
    t2.append(t2[-1]+dt)

print('Vitesse finale visqueux :', vf1)
print('Vitesse finale turbulent :', vf2)

t1_arr = np.array(t1)
v1_arr = np.array(v1)
t2_arr = np.array(t2)
v2_arr = np.array(v2)
fig1, ax1 = plt.subplots()
ax1.scatter(t1_arr/tau1, v1_arr/vf1, marker=".", c="r")
ax1.scatter(t2_arr/tau2, v2_arr/vf2, marker=".", c="b")
plt.show()
