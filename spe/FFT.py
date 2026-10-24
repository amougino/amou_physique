import numpy as np
from matplotlib import pyplot as plt
f0 = 1  # fréquence du signal (Hz)
fe = 40  # fréquence d'échantillonnage
N = 1000  # nombre d'échantillons


def u2(t):
    return (
        2 +
        np.sin(2*np.pi*f0*t) +
        0.5*np.sin(4*np.pi*f0*t) +
        0.2*np.sin(6*np.pi*f0*t)
    )


u = u2

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

amplitude = abs(np.fft.fft(u_discret))
###

plt.subplot(122)
plt.plot(freq, amplitude, 'r-')
plt.plot(freq, amplitude, 'r.')
# plt.xticks(np.arange(0, 11, 1))  # Axe des abscisses : 0, 1, 2,....10
plt.xlim(0, fe/2)
plt.xlabel('fréquence (Hz)')
plt.show()

plt.show()
