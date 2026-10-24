# Programme de Laurent Hache modifié par amou

import numpy as np
from matplotlib import pyplot as plt
f0 = 1  # fréquence du signal (Hz)
fe = 40  # fréquence d'échantillonnage
N = 1000  # nombre d'échantillons


def u1(t):
    return np.sin(2*np.pi*f0*t)


def u2(t):
    return (
        2 +
        np.sin(2*np.pi*f0*t) +
        0.5*np.sin(4*np.pi*f0*t) +
        0.2*np.sin(6*np.pi*f0*t)
    )


def u3(t):
    return (
        2 +
        np.sin(2*np.pi*f0*t) +
        0.5*np.sin(4*np.pi*f0*t) +
        0.2*np.sin(15*np.pi*f0*t)
    )


def u4(t):
    T0 = 1
    u = []
    for i in t:
        if i % T0 < T0 / 2:
            u.append(5)
        else:
            u.append(-5)
    return u


u = u4

t_continu = np.linspace(0, (N-1)/fe, 50000)  # tableau des dates du signal"continu"
u_continu = u(t_continu)
t_discret = np.linspace(0, (N-1)/fe, N)
u_discret = u(t_discret)  # tableau du signal échantillonné
freq = np.linspace(0.0, (N-1)*fe/N, N)  # tableau des fréquences échantillonnées

plt.figure()
plt.subplot(121)
plt.plot(t_continu, u_continu, 'k-')  # graphe signal continu
plt.plot(t_discret, u_discret, 'bo')  # graphe signal échantillonné
plt.xlim(0, 2)
plt.xlabel('t   (s)')
plt.ylabel('amplitude (V)')

real = np.zeros(N)  # partie réelle de la TFD initialisée à 0
img = np.zeros(N)  # partie imaginaire de la TFD initialisée à 0
module_TFD = np.zeros(N)  # tableau des modules de la TFD initialisé

###
for n in range(N):
    for k in range(N):
        real[n] += u_discret[k]*np.cos(2*np.pi*n*k*(1/N))
        img[n] += u_discret[k]*np.sin(-2*np.pi*n*k*(1/N))
    module_TFD[n] = np.sqrt(real[n]**2 + img[n]**2)

amplitude = [module_TFD[n]/N if n == 0 else (module_TFD[n]*2)/N for n in range(N)]
###

plt.subplot(122)
plt.plot(freq, amplitude, 'r-')
plt.plot(freq, amplitude, 'r.')
plt.xticks(np.arange(0, 11, 1))  # Axe des abscisses : 0, 1, 2,....10

plt.xlabel('fréquence (Hz)')
plt.show()

plt.show()
