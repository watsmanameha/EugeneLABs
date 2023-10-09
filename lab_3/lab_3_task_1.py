import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = 3
x_range = np.arange(-1, 1, 0.002)
y_range = np.arange(-1, 1, 0.002)

x, y = np.meshgrid(x_range, y_range)

potential = a * (x**2 + y**2)

dx, dy = np.gradient(potential)
electric_field = np.sqrt(dx**2 + dy**2)

np.savetxt('potential.txt', potential)
np.savetxt('electric_field.txt', electric_field)

fig=plt.figure(figsize=(20, 10))
axes_1 = fig.add_subplot(1, 2, 1, projection='3d')
axes_2 = fig.add_subplot(1, 2, 2, projection='3d')
axes_1.set_xlabel ('x', fontsize =20)
axes_1.set_ylabel ('y',fontsize =20)
axes_1.set_zlabel ('phi', fontsize =20)


axes_1.plot_surface(x, y, potential, cmap='jet')
axes_1.set_title("Phi", fontweight = "bold", fontsize =25)


axes_2.plot_surface(x, y, electric_field, cmap='jet')
axes_2.set_title("E",fontweight = "bold", fontsize =25)
axes_2.set_xlabel  ('x', fontsize =20)
axes_2.set_ylabel  ('y', fontsize =20)
axes_2.set_zlabel  ('E', fontsize =20)
plt.savefig('plot')

print(potential, electric_field)