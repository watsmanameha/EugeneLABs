# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 21:25:28 2023

@author: makar
"""
import math

def calculate_y(x):
    return math.log(x)

def calculate_series(x, eps):
    y = 0
    total_terms = 0
    term = 1
    n = 0

    while abs(term) > eps:
        term = 2 * (((x - 1) ** (2*n+1))/((2*n+1)*(x+1) ** (2*n+1)))
        y += term
        total_terms += 1
        n += 1

    return y, total_terms

def main():
    x_start = float(input("Введите начальное значение аргумента (Xнач): "))
    x_end = float(input("Введите конечное значение аргумента (Xкон): "))
    dx = float(input("Введите шаг (dx): "))
    eps = 1e-4

    print("X\tY\tTotal Terms")
    print("-------------------")

    x = x_start
    while x <= x_end + eps:  # Изменяем условие, чтобы включить x_end в вывод
        y, total_terms = calculate_series(x, eps)
        print(round(x, 2), "\t", round(y, 4), "\t", total_terms)
        x += dx

if __name__ == "__main__":
    main()