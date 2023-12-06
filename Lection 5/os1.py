def gener():
    for i in range(10):
        yield i**2

gen = gener()
for i in range(10):
    print(next(gen))