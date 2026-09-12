import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

mu0 = 4*np.pi*(10**-7)

df = pd.read_csv(os.path.expanduser('~/Desktop/physique/sup/IM/solenoide_mesures_intensite_champ.csv'))

fig, ax = plt.subplots()

ax.plot(df['I'], abs(df['B'])/mu0)

plt.show()
