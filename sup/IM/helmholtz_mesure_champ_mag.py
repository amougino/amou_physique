# centre à 18 cm
# distance entre deux solenoides 9 cm
# centre à 13 cm

# ENSEMBLE DES DISTANCES EN CM

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt


def b1b2(so1, so2, x, R=7):
    d1 = so1 - x
    d2 = so2 - x
    b1_sans_const = (R**2)/(((R**2) + d1**2)**(3/2))
    b2_sans_const = (R**2)/(((R**2) + d2**2)**(3/2))
    return b1_sans_const, b2_sans_const


def B_theo_1_sans_const(so1, so2, x, R=7):
    b1, b2 = b1b2(so1, so2, x, R)
    return b1 + b2


def B_theo_2_sans_const(so1, so2, x, R=7):
    b1, b2 = b1b2(so1, so2, x, R)
    return b1 - b2


df1 = pd.read_csv(os.path.expanduser('~/Desktop/physique/sup/IM/helmholtz_mesures_champ_mag.csv'))

s1_1 = 13.5
s2_1 = 22.5

x1 = np.linspace(start=0, stop=df1['x'][len(df1['x'])-1], num=200)
B_sans1 = B_theo_1_sans_const(s1_1, s2_1, x1)
maxi1 = np.max(B_sans1)
rapport1 = B_sans1 / maxi1


df2 = pd.read_csv(os.path.expanduser('~/Desktop/physique/sup/IM/helmholtz_mesures_champ_mag_anti.csv'))

s1_2 = 8.5
s2_2 = 17.5

x2 = np.linspace(start=0, stop=df1['x'][len(df2['x'])-1], num=200)
B_sans2 = B_theo_2_sans_const(s1_2, s2_2, x2)
maxi2 = np.max(B_sans2)
rapport2 = B_sans2 / maxi2

fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.scatter(df1['x'], -df1['B']/np.max(-df1['B']), label='exp')
ax1.plot(x1, rapport1, label='theo')

ax1.legend()

ax2.scatter(df2['x'], -df2['B']/np.max(-df2['B']), label='exp')
ax2.plot(x2, rapport2, label='theo')

ax2.legend()

plt.show()
