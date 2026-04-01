import numpy as np
import matplotlib.pyplot as plt

R = 1000
C = 0.0000005

f = np.array(
    [50, 100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 40000]
)
Uc = np.array(
    [0.38, 0.71, 1.28, 1.89, 2.19, 2.28, 2.3, 2.32, 2.33, 2.33, 2.33]
)
Ue = np.array(
    [2.48, 2.49, 2.49, 2.41, 2.39, 2.34, 2.33, 2.33, 2.33, 2.33, 2.33]
)
tau = np.array(
    [4.6, 1.95, 0.9, 0.28, 0.08, 0.02, 0.005, 0.001, 0, 0, 0]
) * (10**-3)

f_lin = np.linspace(50, 40000, 1000)

phi1 = tau * 2 * np.pi * f

phi2 = np.arctan(1/(R*C*2*np.pi*f_lin))

H = Uc/Ue

G1 = 20 * np.log10(H)

G2 = 20 * np.log10((R*C*2*np.pi*f_lin)/np.sqrt(1 + (R*C*2*np.pi*f_lin)**2))

fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.set_xlabel("log(f / 1 Hz)")
ax1.set_ylabel("ΔΦ (rad)")

ax1.plot(np.log(f_lin), phi2, label="Déphasage theo", linestyle="dashed", color="orange")
ax1.scatter(np.log(f), phi1, label="Déphasage exp")
ax1.legend()

# ax1.scatter(np.log(f), H, label = "")

ax2.set_xlabel("log(f / 1 Hz)")
ax2.set_ylabel("G (db)")

ax2.plot(np.log(f_lin), G2, label="Gain theo", linestyle="dashed", color="orange")
ax2.scatter(np.log(f), G1, label="Gain exp")
ax2.legend()

plt.show()
