import numpy as np
import matplotlib.pyplot as plt
theta = np.linspace(0, 2*np.pi, 1000) 
r = 1 + (3/4)*np.sin(5*theta)
x = r * np.cos(theta)
y = r * np.sin(theta)
plt.figure(figsize=(6, 6))
plt.title('A simple Flower')
plt.axis('equal')
plt.plot(x, y, color='crimson', linewidth=3, label='r = 1 + (3/4)sin(5θ)')
plt.show()
