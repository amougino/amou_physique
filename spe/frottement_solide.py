import numpy as np


def f_d(m, m_p, h, D):
    return (m_p*h) / ((m + m_p)*D - m_p*h)


m = 0.36
h = 0.68

measures_f_d = [(200, 75), (200, 75), (300, 94), (300, 91.5), (350, 94), (350, 94)]
n_f_d = len(measures_f_d)
f_d_list = np.empty(n_f_d)

for i, (m_p, D) in enumerate(measures_f_d):
    f_d_list[i] = (f_d(m, m_p*0.001, h, D*0.01))

average_d = sum(f_d_list)/n_f_d

dist_d = f_d_list - average_d

s_d = np.sqrt(sum(dist_d**2)/(n_f_d+1))

uncertainty_d = s_d / np.sqrt(n_f_d)

print(f_d_list)
print(average_d, uncertainty_d)


def f_s(alpha):
    return 1/np.tan(alpha)


measures_deg_f_s = np.array([67, 68, 69, 67])
measures_rad_f_s = measures_deg_f_s*(np.pi/180)
n_f_s = len(measures_rad_f_s)
f_s_list = np.empty(n_f_s)

for i, alpha in enumerate(measures_rad_f_s):
    f_s_list[i] = (f_s(alpha))

average_s = sum(f_s_list)/n_f_s

dist_s = f_s_list - average_s

s_s = np.sqrt(sum(dist_s**2)/(n_f_d+1))

uncertainty_s = s_s / np.sqrt(n_f_d)

print(f_s_list)
print(average_s, uncertainty_s)
