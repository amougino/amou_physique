import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

n = 1.5
L = 2.5
R = 1.
hmax = R/n

Nr = 201

fig, ax = plt.subplots(tight_layout=True, figsize=(6, 3))
ax.set_title("Demi-boule d'indice $n={}$".format(n))
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")

for h in np.linspace(-hmax, hmax, Nr):
    i = np.arcsin(h/R)
    r = np.arcsin(n*np.sin(i))
    x = [-L, 0]
    y = [h, h]
    x += [R*np.cos(i)]
    y += [h]
    delta = r - i
    x += [R*np.cos(i) + L*np.cos(delta)]
    y += [h - L*np.sin(delta)]
    plt.plot(x, y, 'r-', alpha=0.1)

ax.plot(n*R/(n-1), 0, 'ko', label="foyer image")

ax.add_patch(Wedge((0, 0), 1, -90, 90, color='lightgray'))
ax.axis('equal')
ax.legend(loc=0)
plt.show()
