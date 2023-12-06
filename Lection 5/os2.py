def ug_chisol(niz, ver, ug_chis):
    if ug_chis < int((niz + ver) / 2):
        ver  = int((niz + ver) / 2)
        ug_chisol(niz, ver, ug_chis)

    elif ug_chis > int((niz + ver) / 2):
        niz = int((niz + ver) / 2)
        ug_chisol(niz, ver, ug_chis)

    elif ug_chis == int((niz + ver) / 2):
        print("Комп угадал число:", ug_chis, "Загаданное число: ", int((niz + ver) / 2))
        

zag_chisol = int(input("Введите число: "))
if zag_chisol > 0 and zag_chisol < 100:
    print("Число введено корректно")
else:
    print("Число введено не верно")

ug_chisol(0, 100, zag_chisol)