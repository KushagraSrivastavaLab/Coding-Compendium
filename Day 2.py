# Given the following relation for the electric field in a plane wave propagating in the z-direction:
# E(z, t) = E * cos(z - t) x̂ + 2 * E * cos(z - t + pi/2) ŷ

# 1) Find the magnetic field ∀ z ∈ [0, 4π], t ∈ [0, 10] using the relation
# B(z, t) = ẑ x E(z, t)
# here we're taking the speed of light be unity just to ease with calculation

# 2) Compute the pointing vector ∀ z and t by the following relation
# S = E x B

# ẑ

import numpy as np
# import matplotlib.pyplot as plt

z = np.linspace(0, 4*np.pi, 100)
t = np.linspace(0, 10, 100)
c = 3 * 10^8

tv, zv = np.meshgrid(t, z)

Ex = np.cos(zv - tv)
Ey = 2 * np.cos(zv - tv + np.pi/2)
Ez = 0 * tv

E = np.array([Ex, Ey, Ez])
E = np.swapaxes(E, 0, -1)
B = c * np.cross(np.array([0, 0, 1]), E)

S = np.cross(E, B)

print(B)