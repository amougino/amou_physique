import numpy as np
import matplotlib.pyplot as plt

mu0 = 4*np.pi*(10**-7)
n = 480
I = 2
R = 0.025


def B(sin3x):
    return (mu0*n*I*0.5*sin3x) / R


fig, ax = plt.subplots()

sin3x = np.sin(np.linspace(-np.pi, np.pi, 1000))**3

ax.plot(sin3x, B(sin3x))

plt.show()
