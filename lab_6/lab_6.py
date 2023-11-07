import numpy as np
import matplotlib.pyplot as plt

# Известные параметры
e = 1.602e-19  # Заряд электрона в Кл
m = 9.109e-31  # Масса электрона в кг
V = 8.5e6  # Начальная скорость электрона в м/c
L = 0.12  # Длина конденсатора в м
R = 0.04  # Радиус внешней обкладки конденсатора в м
r = 0.015  # Радиус внутренней обкладки конденсатора в м

# Расчет разности потенциалов
d = R - r  # Расстояние между обкладками конденсатора в м
V_min = (m * 9.81 * d) / e  # Минимальное значение разности потенциалов, чтобы электрон не вылетел

# Вертикальное ускорение
ay = (e * V_min) / (m * d)

# Время полета до выхода из конденсатора
t = np.sqrt((L / 2) / (0.5 * ay))

# Конечная скорость электрона
V_kon = V + ay * t

# Печать результатов
print("Минимальная разность потенциалов, В:", V_min)
print("Вертикальное ускорение, м/с^2:", ay)
print("Время полета, с:", t)
print("Конечная скорость электрона, м/c:", V_kon)

# Создание временного массива для построения графиков
t_values = np.linspace(0, t, 1000)

# Вычисление зависимостей
y_values = 0.5 * ay * t_values**2
Vy_values = V - ay * t_values
ay_values = np.full_like(t_values, -ay)
y_total_values = 0.5 * ay * t_values**2

# Построение графиков
plt.figure(figsize=(15, 10))

# График y(x)
plt.subplot(2, 2, 1)
plt.plot(y_values, t_values)
plt.title("Зависимость $y(x)$")
plt.xlabel("$y$, м")
plt.ylabel("$x$, м")

# График Vy(t)
plt.subplot(2, 2, 2)
plt.plot(t_values, Vy_values)
plt.title("Зависимость $V_y(t)$")
plt.xlabel("$t$, с")
plt.ylabel("$V_y$, м/c")

# График ay(t)
plt.subplot(2, 2, 3)
plt.plot(t_values, ay_values)
plt.title("Зависимость $a_y(t)$")
plt.xlabel("$t$, с")
plt.ylabel("$a_y$, м/c^2")

# График y(t)
plt.subplot(2, 2, 4)
plt.plot(t_values, y_total_values)
plt.title("Зависимость $y(t)$")
plt.xlabel("$t$, с")
plt.ylabel("$y$, м")

plt.tight_layout()
plt.savefig('plot')
