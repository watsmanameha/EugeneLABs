import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Начальные частоты
freq_x = 100  # Герц
freq_y = 300  # Герц

# Небольшое отличие частот
delta_freq_x = 0.1
delta_freq_y = 0.2

# Временной интервал и количество точек
dt = 0.01
num_points = 1000

# Функция для обновления графика в анимации
def update(frame):
    global freq_x, freq_y

    # Обновление частот с небольшим отличием
    freq_x += delta_freq_x
    freq_y += delta_freq_y

    t = np.linspace(0, 1, num_points)
    x = np.sin(2 * np.pi * freq_x * t)
    y = np.sin(2 * np.pi * freq_y * t)

    # Очищаем предыдущий график и рисуем новый
    plt.clf()
    plt.plot(x, y)
    plt.title(f'Lissajous Figure: {freq_x} Hz vs {freq_y} Hz')

# Создаем анимацию
ani = FuncAnimation(plt.figure(), update, frames=range(100), interval=100)

# Сохраняем анимацию в файл GIF
ani.save('lissajous_animation.gif', writer='pillow', fps=15)
