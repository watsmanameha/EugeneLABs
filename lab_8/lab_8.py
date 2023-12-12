import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = plt.subplot()
plt.plot(0, 0)

t = np.linspace(-2 * np.pi, 2 * np.pi, 200)
initial_frequency_x = 100
initial_frequency_y = 200

def animate(i):
    if i < 500: # Если текущий кадр в первой половине анимации
        frequency_x = initial_frequency_x + 0.01 * i # частота изменяется линейно
        frequency_y = initial_frequency_y # частота по y = const
    else:
        frequency_x = initial_frequency_x + 0.01 * (1000 - i) # Частота по оси x уменьшается линейно с увеличением i от 500 до 1000
        frequency_y = initial_frequency_y
    x = np.sin(frequency_x * t + np.pi/4)
    y = np.sin(frequency_y * t)
    ax.clear()
    plt.plot(x, y, lw='5')
    ax.set_xlabel('Время')
    ax.set_ylabel('Амплитуда')

    return fig,

ani = FuncAnimation(fig, animate, frames=1000, interval=20, blit=False)
