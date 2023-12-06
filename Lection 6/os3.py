import numpy as np
def calculate_area(shape, *args):
    data = {'круг': [1, "print('S = ', np.pi * args[0]**2)"], 'квадрат': [1, "print('S = ', args[0]**2)"], 'прямоугольник': [2, "print('S = ', args[0] * args[1])"], 'треугольник': [2, "print('S = ', 0.5 * args[0] * args[1])"]}
    if shape not in ['круг', 'квадрат', 'прямоугольник', 'треугольник']:
        raise ValueError("Неверное название фигуры")
    if data[shape][0] != len(args):
        raise TypeError("Неверное количество аргументов")
    if len(args) < 0:
        raise ValueError("Нужны положительные числовые аргументы")
    exec(data[shape][1])

calculate_area("треугольник", 4, 7)