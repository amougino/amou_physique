import numpy as np


def fonction(matrice):
    resultats = []
    for i in range(4):
        resultats.append(
            ((matrice[i][0]**2)-(matrice[i][1]**2))/(4*matrice[i][0]))
    sum = 0
    for i in resultats:
        sum += i
    n = len(resultats)
    average = sum/n
    st_dev = 0
    for i in resultats:
        st_dev += (i - average)**2
    st_dev /= n
    st_dev = np.sqrt(st_dev)
    print(2*st_dev / np.sqrt(n))


fonction([[800, 570], [900, 675], [1000, 780], [1100, 885]])
