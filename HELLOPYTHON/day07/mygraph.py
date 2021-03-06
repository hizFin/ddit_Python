from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')
# z = np.linspace(0, 1, 100)
z = np.array([0, 1, 2, 1, 4, 0, 1, 2, 1, 4])
y = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
x = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# x = np.sin(5 * z)0, 0, 0, 0
# y = np.cos(1 * z)

print(z)

ax.plot3D(x, y, z, 'maroon')
ax.set_title('3D line plot')
plt.show()