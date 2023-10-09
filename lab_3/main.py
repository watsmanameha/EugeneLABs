import numpy as np
import matplotlib.pyplot as plt

# Создаем массивы для x и y с заданным шагом
x = np.arange(-1, 1, 0.002)
y = np.arange(-1, 1, 0.002)
dx = 0.002
a = 9

# Создаем сетку для x и y
# x_grid, y_grid = np.meshgrid(x, x)
xx, yy = np.meshgrid(x, x)
phi = np.zeros((len(x), len(y)))

for i in range(len(x)):
    for j in range(len(y)):
        phi[i][j] = a * (x[i] * x[i] - y[j] * y[j])

arr = np.array(phi)

new_phi = -arr
# phi = a * (xx ** 2 - yy ** 2)



# Вычисляем градиент phi по x
Ex, Ey = np.gradient(new_phi, 0.002)
E=Ex+Ey
# Открываем файлы для записи данных
with open('phi.txt', 'w') as file1, open('E.txt', 'w') as file2:
    for i in range(len(x)):
        for j in range(len(y)):
            file1.write(str(phi[i][j]) + '\t')
            file2.write(str(E[i][j]) + '\t')
        file1.write('\n')
        file2.write('\n')

# Создаем график
fig = plt.figure(figsize=(20, 10))

# Добавляем два 3D-подграфика
axes_1 = fig.add_subplot(1, 2, 1, projection='3d')
axes_2 = fig.add_subplot(1, 2, 2, projection='3d')

# Настройка осей и меток
axes_1.set_xlabel('x')
axes_1.set_ylabel('y')
axes_1.set_zlabel('φ')

# Создаем поверхность для phi
axes_1.plot_surface(xx, yy, phi, cmap='cubehelix')
axes_1.set_title("φ")

# Настройка осей и меток для второго графика
axes_2.set_xlabel('x')
axes_2.set_ylabel('y')
axes_2.set_zlabel('E')

# Создаем поверхность для E
axes_2.plot_surface(xx, yy, E, cmap='CMRmap')
axes_2.set_title("E")

# Показываем график
plt.savefig('plot')
# plt.savefig('plot.tiff')
# plt.savefig('plot.raw')
