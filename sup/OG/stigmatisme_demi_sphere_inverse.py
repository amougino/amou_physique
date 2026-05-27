import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

n = 1.5
R = 1
L = 2.5

Nr = 51

fig, ax = plt.subplots(tight_layout=True, figsize=(6, 3))
ax.set_title("Demi-boule d'indice $n={}$".format(n))
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")

for h in np.linspace(-R, R, Nr):
    x_dans_cercle = np.sqrt(R**2 - h**2)
    x = [-L, -x_dans_cercle]
    y = [h, h]
    i = np.arcsin(h/R)
    r = np.arcsin(np.sin(i)/n)
    i_prime = i + r
    y_sortie_cercle = h-x_dans_cercle*np.tan(i_prime)
    if abs(y_sortie_cercle) < 1:
        x += [0]
        y += [y_sortie_cercle]
        r_prime = np.arcsin(n*np.sin(i_prime))
        print(h/R, i_prime)
        x += [L*np.cos(r_prime)]
        y += [L*np.sin(r_prime) + y_sortie_cercle]
    plt.plot(x, y, 'r-', alpha=1)

ax.add_patch(Wedge((0, 0), 1, 90, -90, color='lightgray'))
ax.axis('equal')
ax.legend(loc=0)
plt.show()
