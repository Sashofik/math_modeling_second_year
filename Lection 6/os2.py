def factorial(n):
    if n < 0 or n != int(n):
        raise ValueError("Нужно неотрицательное целое число")
    fact = n
    for i in range(1, n):
          fact = fact * i
    return fact    
    
print(factorial(6))