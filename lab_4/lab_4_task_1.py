import numpy as np
from scipy.integrate import quad


# Заданная функция
def f(x):
    return np.exp(x) * np.sin(x / 2)


# Интеграл с использованием scipy.integrate.quad
true_integral, err = quad(f, 0, np.pi)
print(true_integral, err)

# Метод трапеций
def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral


# Метод Симпсона
def simpsons_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Число n должно быть четным")
    h = (b - a) / n
    integral = f(a) + f(b)
    for i in range(1, n, 2):
        integral += 4 * f(a + i * h)
    for i in range(2, n - 1, 2):
        integral += 2 * f(a + i * h)
    integral *= h / 3
    return integral


# Точность (1%)
tolerance = 0.01 * true_integral

# Начнем с небольшого значения n и будем увеличивать его до достижения нужной точности
n_trap = 2  # Начальное значение n для метода трапеций
n_simp = 4  # Начальное значение n для метода Симпсона

while True:
    result_trap = trapezoidal_rule(f, 0, np.pi, n_trap)
    result_simp = simpsons_rule(f, 0, np.pi, n_simp)

    if abs(result_trap - true_integral) <= tolerance:
        print(f"Метод трапеций: n = {n_trap}, результат = {result_trap}")

    if abs(result_simp - true_integral) <= tolerance:
        print(f"Метод Симпсона: n = {n_simp}, результат = {result_simp}")

    if abs(result_trap - true_integral) <= tolerance and abs(result_simp - true_integral) <= tolerance:
        break

    n_trap *= 2
    n_simp *= 2
