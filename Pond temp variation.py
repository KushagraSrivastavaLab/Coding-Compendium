# Today i worked with Newtons Law of Cooling.
# The scenario is that we have a pond with shallow water and we want to model the temperature of the water over time, given the outside temperature data.

# Equation of the Newton's Law of Cooling:
# dT/dt = -k * (T - Ts(t))
# we are taking k = 0.5 and Ts(t) is the outside temperature at time t.

# Objective:
# To plot the temperature of shallow water in a pond over time, given the outside temperature data.

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.interpolate import interp1d

# Outside temperature data (in Kelvin) at different times (in hours)

t_m = np.array([ 0.,   1.04347826,   2.08695652,   3.13043478,
          4.17391304,   5.2173913 ,   6.26086957,   7.30434783,
          8.34782609,   9.39130435,  10.43478261,  11.47826087,
         12.52173913,  13.56521739,  14.60869565,  15.65217391,
         16.69565217,  17.73913043,  18.7826087 ,  19.82608696,
         20.86956522,  21.91304348,  22.95652174,  24.])
temp_m = np.array([273.        , 296.95463138, 318.731569  , 338.33081285,
        355.75236295, 370.99621928, 384.06238185, 394.95085066,
        403.66162571, 410.19470699, 414.55009452, 416.72778828,
        416.72778828, 414.55009452, 410.19470699, 403.66162571,
        394.95085066, 384.06238185, 370.99621928, 355.75236295,
        338.33081285, 318.731569  , 296.95463138, 273.       ])

# I found the above data by using the following code:
# In this code, I created a quadratic function to model the outside temperature over time. 
# # x = np.linspace(0, 24, 24)
# y = -x**2 + 24 * x + 273
# points = np.stack((x, y), axis=1).T

Ts = interp1d(t_m, temp_m, kind='cubic')

def dTdt(T, t):
    return -0.5 * (T - Ts(t))

time = np.linspace(1, 23, 100)
T0 = 296.00000002
sol = odeint(dTdt, T0, time).T[0]

plt.plot(time, sol, label='Shallow Water Temperature')
plt.scatter(t_m, temp_m, color='red', label='Outside Temperature')

plt.xlabel('Time (hours)')
plt.ylabel('Temperature (K)')
plt.title('Comparison of Shallow Water and Outside Temperatures')
plt.legend()

plt.show()

# After looking at the plt, that the maximum temperature of the water is not when the outside temperature is maximum.
# This is because the water takes time to heat up and cool down, so there is a lag between the outside temperature and the water temperature. 
# The water temperature will continue to rise even after the outside temperature has started to decrease
# It will also take time for the water to cool down after the outside temperature has dropped. 
# This is a common phenomenon in thermal systems where there is a delay in response due to heat capacity and thermal inertia.
