# Today, i thought of solving a pair of coupled differential equation with the help of SciPy.

# Equations:
# y1' = y1 + y2**2 + 3*x
# y2' = 3*y1 + y2**3 - np.cos(x)

# Given,
# y1(0) = 0
# y2(0) = 0

# S = (y1, y2) 

# Objective: 
# To solve the above pair of coupled differential equations using SciPy's odeint function.
# Plot the graph of the solution of the equations

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def dSdx(S, x):
    y1, y2 = S
    return [y1 + y2**2 + 3*x, 3*y1 + y2**3 - np.cos(x)]

# Still not sure, why and how does this initial guess work
y1_0 = 0
y2_0 = 0
S_0 = [y1_0, y2_0]

x = np.linspace(0, 1, 100)
sol = odeint(dSdx, S_0, x)

y1 = sol[:, 0]
y2 = sol[:, 1]

print(y1)
print(y2)

plt.plot(x, y1, label='y1')
plt.plot(x, y2, label='y2')
plt.show()
