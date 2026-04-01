import numpy as np
import sup.approx as ap


def moy(val_l):
    sum = 0
    for i in val_l:
        sum += i
    return sum / len(val_l)


g = 9.8
mt = 67.24 * (10**-3)
lt = 46 * (10**-2)
mm = 229.47 * (10**-3)

# 1 -> 30 cm

lm_1 = 30 * (10**-2)
w0_1 = np.sqrt(
    1.5 * g * (((2*lm_1*mm) + (lt*mt)) / ((mt*(lt**2)) + (3*mm*(lm_1**2))))
)
T0_theo_1 = (2*np.pi) / w0_1

T0_exp_l_1 = [1.09, 1.09, 1.10, 1.10]
T0_exp_1 = moy(T0_exp_l_1)

# 2 -> 40 cm

lm_2 = 40 * (10**-2)
w0_2 = np.sqrt(
    1.5 * g * (((2*lm_2*mm) + (lt*mt)) / ((mt*(lt**2)) + (3*mm*(lm_2**2))))
)
T0_theo_2 = (2*np.pi) / w0_2

T0_exp_l_2 = [1.23, 1.25, 1.25, 1.24]
T0_exp_2 = moy(T0_exp_l_2)

# 3 -> 10 cm

lm_3 = 10 * (10**-2)
w0_3 = np.sqrt(
    1.5 * g * (((2*lm_3*mm) + (lt*mt)) / ((mt*(lt**2)) + (3*mm*(lm_3**2))))
)
T0_theo_3 = (2*np.pi) / w0_3

T0_exp_l_3 = [0.87, 0.85, 0.86, 0.85]
T0_exp_3 = moy(T0_exp_l_3)

# 4 -> 20 cm

lm_4 = 20 * (10**-2)
w0_4 = np.sqrt(
    1.5 * g * (((2*lm_4*mm) + (lt*mt)) / ((mt*(lt**2)) + (3*mm*(lm_4**2))))
)
T0_theo_4 = (2*np.pi) / w0_4

T0_exp_l_4 = [0.95, 0.97, 0.96, 0.96]
T0_exp_4 = moy(T0_exp_l_4)

print(T0_theo_1, T0_theo_2, T0_theo_3, T0_theo_4)
print(T0_exp_1, T0_exp_2, T0_exp_3, T0_exp_4)

x = [30, 40, 10, 20]
y = [T0_exp_1, T0_exp_2, T0_exp_3, T0_exp_4]


def F(x, variables):
    return (variables[0]*x + variables[1])


s = ap.Approx(F, x, y, [0.1, 0.1], [0.5, 0.5], 0.99)
for x in range(500):
    s.step()
    print(s.vars)

# POUR lm = 0
w0_5 = np.sqrt(
    1.5 * g * (lt*mt) / (mt*(lt**2))
)
T0_theo_5 = (2*np.pi) / w0_5
print(T0_theo_5)
