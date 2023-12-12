import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Исходные частоты
freq_x = 100  # Частота по оси X в Герцах
freq_y = 300  # Частота по оси Y в Герцах

# Создание фигуры Лиссажу
def lissajous(t, freq_x, freq_y):
    x = np.sin(2 * np.pi * freq_x * t)
    y = np.sin(2 * np.pi * freq_y * t)
    return x, y

def update(frame):
    plt.clf()
    t = np.linspace(0, frame / 10, 1000)  # Используйте больше или меньше 10, чтобы изменить скорость анимации
    x, y = lissajous(t, freq_x, freq_y)
    plt.plot(x, y)
    plt.title(f'Lissajous Figure (Time: {t[-1]:.1f} s)')
    plt.xlabel('X-axis (units)')
    plt.ylabel('Y-axis (units)')

# Создание анимации
fig, ax = plt.subplots()
ani = FuncAnimation(fig, update, frames=np.arange(0, 1000), interval=50)

ani.save('lissajous_animation.gif', writer='pillow', fps=15)
