import numpy as np
import matplotlib.pyplot as plt

taille_15_crans = 13.7
l_eprouv = taille_15_crans * (5/3)

vol_glyc = 250 * (10**-6)
mass_glyc = (393.02 - 88.21) * (10**-3)

C_glyc = np.array([0, 20, 40, 60, 80, 92, 96, 100])
visc_glyc = np.array([1.004, 1.766, 3.73, 10.9, 60.6, 319, 648, 1460])
RHOGLYC = mass_glyc / vol_glyc
CONST_g = 9.8


def visc(rhob, diamb, fall_dist, dt):
    viscosity = ((rhob - RHOGLYC)*(diamb**2)*CONST_g) / (18*(fall_dist/dt))
    return viscosity


def average(array):
    total = 0
    for obj in array:
        total += obj
    return (total/len(array))


def stan_dev(array):
    av = average(array)
    res = 0
    for obj in array:
        res += (obj - av)**2
    res *= (1/(len(array) - 1))
    return (np.sqrt(res))


def accuracy_a(array):
    standard_deviation = stan_dev(array)
    return (standard_deviation / np.sqrt(len(array)))

# *** MEASUREMENTS ***


# SMALL BALL
diam_small = 4.97 * (10**-3)
vol_small = ((diam_small/2)**3) * np.pi * (4/3)
mass_small = 0.51 * (10**-3)
rho_small = mass_small / vol_small
dt_small = [2.69, 2.91, 2.68, 2.71, 2.78, 2.69, 2.66, 2.69, 2.72, 2.75]

arr_dt_small = np.array(dt_small)

visc_calc_small = visc(rho_small, diam_small, l_eprouv, arr_dt_small)

av_small = visc_calc_small

# BIG BALL
diam_big = 6.97 * (10**-3)
vol_big = ((diam_big/2)**3) * np.pi * (4/3)
mass_big = 1.4 * (10**-3)
rho_big = mass_big / vol_big
dt_big = [1.75, 1.78, 1.69, 1.79, 1.84, 1.84, 1.65, 1.69, 1.75, 1.66]

arr_dt_big = np.array(dt_big)

visc_calc_big = visc(rho_big, diam_big, l_eprouv, arr_dt_big)

# RESULTS
print('\n')

total_visc = np.concatenate((visc_calc_small, visc_calc_big))
print('Moyenne viscosite petite bille :', average(visc_calc_small))
print('Moyenne viscosite grosse bille :', average(visc_calc_big))
print('Moyenne viscosite total:', average(total_visc))
print('Ecart type viscosite petite bille :', stan_dev(visc_calc_small))
print('Ecart type viscosite grosse bille :', stan_dev(visc_calc_big))
print('Ecart type viscosite total :', stan_dev(total_visc))
print('Incertitude a viscosite petite bille :', accuracy_a(visc_calc_small))
print('Incertitude a viscosite grosse bille :', accuracy_a(visc_calc_big))
print('Incertitude a viscosite total :', accuracy_a(total_visc))
print('visc', visc(rho_big, diam_big, l_eprouv, 1.53))
print('\n')

print(diam_big, vol_big, mass_big, rho_big, l_eprouv/dt_big)

# PLOTTING

fig1, ax1 = plt.subplots()
ax1.scatter(dt_small, visc_calc_small, c="r")
ax1.scatter(dt_big, visc_calc_big, c="b")

fig2, ax2 = plt.subplots()
ax2.scatter(C_glyc, np.log(visc_glyc), c="r")
ax2.axhline(y=np.log((10**3)*average(visc_calc_small)), c='b')
ax2.axhline(y=np.log((10**3)*average(visc_calc_big)), c='r')
ax2.axhline(y=np.log((10**3)*average(total_visc)), c='black')

plt.show()
