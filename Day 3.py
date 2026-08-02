# Today I got my hands on a beautiful mathematical function
# So I decided to work around it a bit.

# The function is f(x, y) = e^(-(x^2 + y^2)) * sin(x)

# Objectives:
# 1) Create a contour plot of the function f(x, y) over the range x ∈ [-2, 2] and y ∈ [-2, 2].
# 2) Finding the volume of |f(x, y)| in the specified x and y range
# 3) Finding the volume of |f(x, y)| where (x**2 + y**2)**(1/2) > 0.5


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 300)
y = np.linspace(-2, 2, 300)
xv, yv = np.meshgrid(x, y)

f = np.exp(-(xv**2 + yv**2))*np.sin(xv)

plt.contourf(xv, yv, f, levels=20, cmap='viridis')
plt.colorbar(label='Function Value')
plt.title('Contour Plot of $f(x, y) = e^{-(x^2 + y^2)}\\sin(x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Volume of |f(x, y)| over the specified range
print(np.abs(f.ravel()).sum() * np.diff(x)[0] * np.diff(y)[0] )

# Volume of |f(x, y)| where (x**2 + y**2)**(1/2) > 0.5
print(np.abs(f[xv**2 + yv**2 > 0.5**2].ravel()).sum() * np.diff(x)[0] * np.diff(y)[0] )  

# If you will look closely towards the graph
# You will see that the function is showing two humps, one +ve and the other one -ve. 
# Again just the previous day, This is another plot, that would look great if plotted in 3D, but as I haven't studied that yet, so will definitely try this question again too