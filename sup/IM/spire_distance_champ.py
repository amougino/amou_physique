'''
centre spire quand teslametre à 19cm (niveau sorti solenoide)
'''

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

mu0 = 4*np.pi*(10**-7)

df = pd.read_csv(os.path.expanduser('~/Desktop/physique/sup/IM/spire_mesures_distance_champ.csv'))

fig, ax = plt.subplots()


def H(x, n=480, I=2, R=0.025):
    return (n*I*0.5)*((R**2)/(np.sqrt((R**2)+(x**2))**3))


x_exp = 19-df['x']
ax.scatter(x_exp, (abs(df['B'])*(10**-6))/mu0)
x = np.linspace(min(x_exp), max(x_exp), 200)
ax.plot(x, H(x*0.01))

plt.show()
