import numpy as np
import matplotlib.pyplot as plt

R = 1 * (10**3)
C = 0.5 * (10**-6)

f = np.array(
    [50, 100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 40000]
)
Uc = np.array(
    [3.4, 3.33, 2.93, 2.13, 1.23, 0.65, 0.350, 0.203, 0.123, 0.081, 0.066]
)
Ue = np.array(
    [3.53, 3.53, 3.5, 3.43, 3.4, 3.4, 3.39, 3.36, 3.35, 3.34, 3.34]
)
tau = np.array(
    [-0.5, -0.5, -0.490, -0.380, -0.254, -0.138, -0.073, -0.038, -0.019, -0.010, -0.006]
) * (10**-3)

phi = tau * 2 * np.pi * f

H = Uc/Ue

G1 = 20 * np.log10(H)

G2 = 20 * np.log10(1/np.sqrt(1 + (R*C*2*np.pi*f)**2))

fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.set_xlabel("log(f / 1 Hz)")
ax1.set_ylabel("ΔΦ (rad)")

ax1.scatter(np.log(f), phi, label="Déphasage")
ax1.legend()

# ax1.scatter(np.log(f), H, label = "")

ax2.set_xlabel("log(f / 1 Hz)")
ax2.set_ylabel("G (db)")

ax2.scatter(np.log(f), G1, label="Gain exp")
ax2.scatter(np.log(f), G2, label="Gain theo")
ax2.legend()

plt.show()

# Pour la prochaine fois : line pleine
