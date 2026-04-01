import sup.approx as ap
import numpy as np

m = 0.2
T_1_exp_3 = [1.27, 1.26, 1.26, 1.27]
T_1_exp_4 = [1.51, 1.53, 1.51, 1.52]
T_1_exp_5 = [1.78, 1.78, 1.77, 1.76]
T_1_exp_6 = [2.03, 2.04, 2.04, 2.04]
T_1_exp_7 = [2.32, 2.32, 2.34, 2.35]
T_1_exp_8 = [2.60, 2.62, 2.63, 2.61]


def moy(values):
    sum = 0
    for i in values:
        sum += i
    return sum / len(values)


d = [i*(10**-2) for i in range(3, 9)]

T_1_exp = [
    moy(T_1_exp_3),
    moy(T_1_exp_4),
    moy(T_1_exp_5),
    moy(T_1_exp_6),
    moy(T_1_exp_7),
    moy(T_1_exp_8)
]
print(T_1_exp)


def T_1(d, variables):  # variables : I0, C
    return 2*np.pi*np.sqrt(
        (variables[0] / variables[1]) +
        (2 * m * ((d**2) / variables[1]))
    )


s = ap.Approx(T_1, d, T_1_exp, [0.00001, 0.001], [0.0001, 0.01], 0.98)
for x in range(100000):
    s.step()
print(s.vars)


ds = d = [(i*(10**-2))**2 for i in range(3, 9)]
T_1_exp_s = []
for i in T_1_exp:
    T_1_exp_s.append(i**2)


def T_1_s(d_squared, variables):  # variables : a, b
    return variables[0]*d_squared + variables[1]


t = ap.Approx(T_1_s, ds, T_1_exp_s, [10, 0.1], [900, 0.5], 0.98)
for x in range(100000):
    t.step()
# print(t.vars)
print([
    (t.vars[1]*2*m)/t.vars[0],
    2*m*4*(np.pi**2)/t.vars[0]
])
