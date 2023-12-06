import numpy as np

class ZnakError(Exception):
    def __str__(self):
        return 'Неправильный знак'

class ChislError(Exception):
    def __str__(self):
         return 'Неправильная запись числа'  
         
prot = None
prznak = None
prchis = None
while True:
    while True:
        try:
            if prot != None and prznak != None and prchis != None:
                chisl1 = prot
                znak = prznak
                chisl2 = prchis
            elif prot != None and prznak != None and prchis == None:
                chisl1 = prot
                znak = str(input("Введите операцию(степень это **): "))                
                if znak not in ["+", "-", "*", "/", "%", "**", "//", ]:
                    raise ZnakError()
                chisl2 = float(input("Введите 2 число: "))
            elif prot == None and prznak == None and prchis == None:
                chisl1 = float(input("Введите 1 число: "))
                znak = str(input("Введите операцию(степень это **): "))
                if znak not in ["+", "-", "*", "/", "%", "**", "//", ]:
                    raise ZnakError() 
                chisl2 = float(input("Введите 2 число: "))               
            else:
                chisl1 = float(input("Введите 1 число: "))
                znak = str(input("Введите операцию(степень это **): "))
                if znak not in ["+", "-", "*", "/", "%", "**", "//", ]:
                    raise ZnakError()
            break

        except ZeroDivisionError:
            print("Произошло деление на ноль, замените 2 число")
            continue
        except ZnakError:
            print("Произошло постановка неправильного знака, замените знак")
            continue
        except Exception as e:
            print("Произошло непридвиденная ошибка, повторите запрос")
            continue
    prot = None
    prznak = None
    prchis = None
    exec("otvet = chisl1 {} chisl2".format(znak))
    print(chisl1, znak, chisl2, "=",  otvet)
    ot = str(input("Повторить операцию Enter, оставить ответ z, очистить o, в случае если зотите закрыть калькулятор, напишите что угодно: "))
    print(ot)
    if ot == 'o':
        ot = ''
        continue
    elif ot == '':
        prot = otvet
        prznak = znak
        prchis = chisl2
        ot = ''
        continue
    elif ot == 'z':
        prot = otvet
        prznak = znak
        ot = ''
        continue
    else:
        break