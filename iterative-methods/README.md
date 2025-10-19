# Simple Iteration Method

Решение систем линейных уравнений методом простых итераций.

## Использование

```python
from src.simple_iteration_method import IterativeSolver

# Система: 2x + y = 5, x + 3y = 5
A = [[2, 1], [1, 3]]  # матрица коэффициентов
b = [5, 5]            # правая часть
x0 = [0, 0]           # начальное приближение

solver = IterativeSolver(
    A=A,              # матрица системы
    n=2,              # размерность
    b=b,              # вектор b
    x0=x0,            # начальное приближение  
    tau=0.3,          # параметр релаксации
    tolerance=1e-8,   # точность
    Nmax=100          # макс. итераций
)

solver.preprocess()   # проверка и подготовка данных
solution, iterations, error = solver.Solver()  # решение

print(f"Решение: {solution}")      # найденное решение
print(f"Итераций: {iterations}")   # количество итераций
print(f"Ошибка: {error}")          # конечная ошибка