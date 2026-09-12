import numpy as np
import matplotlib.pyplot as plt


def e(t, T=3*10**-3, a=2/3, min=0, max=4.5):
    r = []
    for i in t:
        if i % T <= T*a:
            r.append(max)
        else:
            r.append(min)
    return r


H0 = 0.5
wc = 200
tau = 1/wc

fe = 10000
Te = 1/fe

N = 200

tn = np.linspace(0, Te*N, N)
en = e(tn)
sn = [1]

for i in range(0, len(en)-1):
    sn.append((H0*(Te/tau)*en[i]) + ((1-(Te/tau))*sn[-1]))

fig, ax = plt.subplots()

plt.plot(tn, en)
plt.plot(tn, sn)

plt.show()
