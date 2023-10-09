# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 21:25:28 2023

@author: makar
"""
import math

x_start = float(input("Введите начальное значение аргумента : ")) # x>0
x_end = float(input("Введите конечное значение аргумента: "))
dx = float(input("Введите шаг dx: "))
eps = 1e-4

def func(x):
    return math.log(x) #вызываем вычисления ряда

def calculate_series(x_start, x_end, dx, eps): #данная функция вычисляет ряд значений функции
    print("Аргумент   Значение функции   Количество членов ряда")
    x = x_start #переменная x инцелизируется x_start 
    while x <= x_end:#цикл выполняется до тех пор, пока x не превысит конечное значение аргумента
        term = x #текущий член ряда
        result = term #результат суммы членов ряда
        num_terms = 1 #количество членов ряда
        while abs(term) > eps: #выполняется до тех пор,пока значение текущего члена ряда term не станет меньше или равно точности eps.
            num_terms += 1 #учитываем новый член ряда
            term *= (x - 1) / num_terms #получаем следующий ряд члена
            #Ограничение больших чисел 
            if abs(term) > 1000:
                break
            result += term #обновление суммы членов
        print(f"{x}\t\t{func(x)}\t\t{num_terms}")
        x += dx


calculate_series(x_start, x_end, dx, eps)