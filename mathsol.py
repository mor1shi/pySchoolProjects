import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3 + x - 1

def bisection_method(a, b, E):
    count = 0
    iterations = []
    roots = []
    
    while True:
        c = (a + b) / 2
        fa = f(a)
        fc = f(c)
        
        iterations.append(count)
        roots.append(c)
        
        if abs(fc) < E:
            print(f"Решение найдено: x = {c}, f(x) = {fc}")
            break
        
        if fa * fc < 0:
            b = c
        else:
            a = c
        
        count += 1
        
        # Защита от бесконечного цикла
        if count > 1000:
            print("Достигнуто максимальное количество итераций.")
            break
    
    return c, iterations, roots

def plot_function_and_process(a, b, E):
    # Настройка графика функции
    x_vals = np.linspace(a, b, 400)
    y_vals = f(x_vals)
    
    plt.figure(figsize=(12, 6))
    
    # График функции
    plt.subplot(1, 2, 1)
    plt.plot(x_vals, y_vals, label='f(x) = x³ + x - 1')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('График функции')
    plt.grid(True)
    plt.legend()
    
    # Находим корень методом бисекции
    root, iterations, roots = bisection_method(a, b, E)
    
    # График процесса сходимости
    plt.subplot(1, 2, 2)
    plt.plot(iterations, roots, 'o-', label='Приближения корня')
    plt.axhline(root, color='red', linestyle='--', label='Найденный корень')
    plt.xlabel('Итерация')
    plt.ylabel('Значение корня')
    plt.title('Процесс сходимости метода бисекции')
    plt.grid(True)
    plt.legend()
    
    plt.tight_layout()
    plt.show()

# Ввод данных
a = float(input("Введите a: "))
b = float(input("Введите b: "))
E = float(input("Введите точность E: "))

# Проверка условия f(a)*f(b) < 0
if f(a) * f(b) >= 0:
    print("На интервале [a, b] функция не меняет знак. Возможно, корня нет или их несколько.")
else:
    plot_function_and_process(a, b, E)
