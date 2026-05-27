import numpy as np
import matplotlib.pyplot as plt

frequence_t = [i*200 + 100 for i in range(8)] + [i*50 + 1550 for i in range(12)] + [
    i*200 + 2300 for i in range(3)]  # Hz
tension = [40, 40, 45, 45, 55, 60, 90, 140, 180, 210,
           260, 330, 400, 340, 310, 260, 220, 190, 170, 130, 120, 90, 80]  # mV
frequence_d = [i*200 + 700 for i in range(5)] + [i*50 + 1550 for i in range(12)] + [
    i*200 + 2300 for i in range(3)]  # Hz
decalage = [1120, 850, 690, 600, 530, 530, 520,
            510, 510, 10, 30, 60, 70, 80, 90, 100, 100, 105, 100, 90]  # micro s

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

ax1.set_title("Circuit RLC 1 kOhm, 1 H, 8 nF, 0.5 V")
ax1.set_xlabel("f (Hz)")
ax1.set_ylabel("Tension (mV)", color="red")

tension_gen = 500  # mV
tension_arr = np.array(tension)

ax1.scatter(
    frequence_t,
    tension_arr,
    color="red",
    label="U"
)
ax1.plot(
    [0, 2700],
    [(400/np.sqrt(2)), (400/np.sqrt(2))],
    color="green",
    label="bande passante U_max / √2"
)
ax1.legend()

dephasage = [(2*np.pi*decalage[i]*(10**-6)*frequence_d[i] + np.pi) % (2*np.pi) - np.pi
             for i in range(len(decalage))]

ax2.set_xlabel("f (Hz)")
ax2.set_ylabel("Déphasage (rad)", color="blue")

ax2.scatter(
    frequence_d,
    dephasage,
    color="blue",
    label="ΔΦ"
)
ax2.legend()

plt.show()

fig.savefig("MOUGINOT_BOLLINGER_TP_resonance.pdf")
