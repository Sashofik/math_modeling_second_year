def ug_chisol(niz, ver, ug_chis):
    print(niz, ver)
    print(int(ver / 2))
    if ug_chis < int(ver / 2):
        ver  = int(ver / 2)
        ug_chisol(niz, ver, ug_chis)

    elif ug_chis > int(ver / 2):
        niz = int(ver / 2)
        ug_chisol(niz, ver, ug_chis)

    elif ug_chis == int(ver / 2):
        print("Комп угадал число:", ug_chis, "Загаданное число: ", int(ver / 2))
        

zag_chisol = int(input("Введите число: "))
if zag_chisol > 0 and zag_chisol < 100:
    print("Число введено корректно")
else:
    print("Число введено не верно")

ug_chisol(0, 100, zag_chisol)