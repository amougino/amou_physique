import numpy as np
import matplotlib.pyplot as plt

k = 4  # N . m-1
m = 0.1  # kg
fs = 0.7
fd = 0.4
g = 9.81  # m . s-2
v0 = 1  # m . s-1

w = np.sqrt(k/m)
c = fd*g  # abs( frottement dynamique massique )

'''

Equation differentielle :
d^2x/dt^2 + w^2 * x = w^2 * v0 * t - c

'''

n_points = 100000
final_time = 4  # s
Te = final_time / n_points

t = np.linspace(0, final_time, n_points + 1)  # pour avoir 0 ET la date finale

fig = plt.figure(figsize=(12, 8))

'''
Question 5
Sans retour en arrière
'''

x = np.zeros(n_points + 1)
v = np.zeros(n_points)
fr = np.zeros(n_points + 1)  # force de frottement


for n in range(2, n_points + 1):

    t_curr = Te*(n-1)
    x_prev, x_curr = x[n-2], x[n-1]

    l = v0*t_curr - x_curr
    v[n-1] = (x_curr - x_prev) / Te

    if v[n-1] > 0 or k*l > fs*m*g:
        x_next = 2*x_curr - x_prev + Te**2 * (w**2 * l - c)
        fr[n] = -m*c
        x[n] = max(x_next, x_curr)  # pour eviter retour en arrière
    else:
        x[n] = x_curr
        fr[n] = -k*l

ax1 = plt.subplot2grid((2, 3), (0, 0))
ax2 = plt.subplot2grid((2, 3), (0, 1))
ax3 = plt.subplot2grid((2, 3), (0, 2))

ax1.plot(t, x)
ax1.set_title("Position")

ax2.plot(t[1:], v)
ax2.set_title("Vitesse")

ax3.plot(t, fr)
ax3.set_title("Force de frottement")

ax1.grid()
ax2.grid()
ax3.grid()

'''
Question 6
Avec retour en arrière
'''

x2 = np.zeros(n_points + 1)
v2 = np.zeros(n_points)
fr2 = np.zeros(n_points + 1)  # force de frottement


for n in range(2, n_points + 1):

    t_curr = Te*(n-1)
    x_prev, x_curr = x2[n-2], x2[n-1]

    l = v0*t_curr - x_curr
    F = k*l  # force ressort
    v_curr = (x_curr - x_prev) / Te
    v2[n-1] = v_curr

    if v_curr != 0:
        direction = np.sign(v_curr)
    elif abs(F) > fs*m*g:
        direction = np.sign(F)
    else:
        direction = 0  # collé

    if direction == 0:
        x2[n] = x_curr
        fr2[n] = -F
    else:
        x_next = 2*x_curr - x_prev + Te**2 * (w**2 * l - direction*c)
        if v_curr != 0 and np.sign(x_next - x_curr) != direction:
            # si le bloc change de direction, alors à un moment v = 0 (statique)
            # alors on l'arrete pour repasser par ce moment de collé
            x_next = x_curr
        x2[n] = x_next
        fr2[n] = -m*c*direction

ax4 = plt.subplot2grid((2, 3), (1, 0))
ax5 = plt.subplot2grid((2, 3), (1, 1))
ax6 = plt.subplot2grid((2, 3), (1, 2))

ax4.plot(t, x2)
ax4.set_title("Position avec retour arriere")

ax5.plot(t[1:], v2)
ax5.set_title("Vitesse avec retour arriere")

ax6.plot(t, fr2)
ax6.set_title("Force de frottement avec retour arriere")

ax4.grid()
ax5.grid()
ax6.grid()


plt.show()
