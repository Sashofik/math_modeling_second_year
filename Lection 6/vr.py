#	
#def element_i(obj, i):
#    return obj[i]
#
#x = [0, 1, 2, 3]
#
#print(element_i(x, 3))
 
#print(element_i(x, 4))
#	
#def catcher():
#    try:
#        print(element_i(x, 4))
#    except IndexError:
#        print('Я получил исключение')
#    print('Сделано, продолжаем')
#
#catcher()
#
#try:
#    # Некоторый код, генерирующий исключение
#    raise Exception("Описание ошибки")
#    # raise ExceptionType("Optional message")
#except Exception as e:
#    print("Произошла ошибка:", str(e))
# raise ValueError
#try:
#    raise KeyError  # Генерация исключения вручную
#except KeyError:
#    print('Я сгенерировал ошибку!')#
#
#class MyError(Exception):
#    def __str__(self):
#        return 'Натворил делов'
# 
#raise MyError()

for i in range(10):
    assert i == 7, "Error"