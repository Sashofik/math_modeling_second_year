def zamenitel(a):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return a + args[0]
        return wrapper
    return decorator

@zamenitel(4)
def dec2(b):
    return b + 8

print(dec2(3))