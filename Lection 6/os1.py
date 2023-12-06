def square_root(x):
    if x < 0:
        raise ValueError("Нельзя извлекать корень из отрицательного числа")
    return x**0.5

print(square_root(54))