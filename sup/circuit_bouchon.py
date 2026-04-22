import numpy as np
import matplotlib.pyplot as plt

f = np.array(
    [25*i + 50 for i in range(27)]
)
U_s = np.array(
    [2.78, 2.6, 2.44, 2.25, 1.99, 1.71, 1.39, 1.07, 0.76, 0.5, 0.38, 0.51, 0.74, 0.97, 1.2, 1.45, 1.61, 1.79, 1.95, 2.1, 2.22, 2.32, 2.4, 2.52, 2.6, 2.7, 2.76]
)
U_e = np.array(
    [3.85, 3.85, 3.86, 3.86, 3.88, 3.9, 3.9, 3.92, 3.94, 3.94, 3.94, 3.94, 3.94, 3.94, 3.94, 3.94, 3.92, 3.92, 3.90, 3.90, 3.90, 3.89, 3.88, 3.88, 3.88, 3.86, 3.86]
)

fig, ax = plt.subplots()

G = 20*np.log10(U_s/U_e)

ax.plot(f, G, label="gain exp")
ax.plot([f[0], f[-1]], [-3, -3], label="coupure")

ax.legend()

plt.show()
