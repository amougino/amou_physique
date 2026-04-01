#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created 2026-03-10

@author: romain.berthelard

In this program, m = 1kg and therefore never appears.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# Functions
def force(r, n, k=1):
    """
    Parameters
    ----------
    r : distance from origin
    n : integer (0 or 1 forbidden)
    k : constant for attractive (k>0) or repulsive (k<0) force
        Default is 1.

    Returns
    -------
    radial component of the force

    """
    return -k/r**n


def fun(t, y):      # y[0] = r ; y[1] = theta ; y[2] = v_r
    """
    Parameters
    ----------
    t : TYPE
        DESCRIPTION.
    y : TYPE
        DESCRIPTION.
    force: force law which moves the system

    Returns
    -------
    None.

    """
    global L0   # angular momentum
    ydot = [0, 0, 0]
    ydot[0] = y[2]                          # dr/dt = v_r
    ydot[1] = L0/y[0]**2                    # dtheta/dt = L0/r^3
    # dv_r/dt = forces + momentum^2/r^3
    ydot[2] = force(y[0], -1, k=1) + L0**2/y[0]**3
    return ydot


# Parameters
t_max = 10
N_step = 3000000000
r0, v0 = 1, 0.5          # initial condition
L0 = r0*v0                      # velocity is orhogonal to radius

# Solving mouvement equations
sol = solve_ivp(fun, [0, t_max],
                [r0, 0, 0],         # r(0), theta(0) and v_r(0)
                t_eval=np.linspace(0, t_max, N_step),
                rtol=1e-9)

# Plotting movement
fig, ax = plt.subplots(figsize=(5, 4), tight_layout=True)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")

ax.plot(sol.y[0]*np.cos(sol.y[1]), sol.y[0]*np.sin(sol.y[1]), color='b')
ax.scatter(0, 0, color='k')
ax.axis('equal')

plt.show()
