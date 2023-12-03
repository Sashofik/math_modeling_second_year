prot = None
prznak = None
prchis = None
while True:
    if prot != None and prznak != None and prchis != None:
        chisl1 = prot
        znak = prznak
        chisl2 = prchis
    elif prot != None and prznak != None and prchis == None:
        chisl1 = prot
        znak = str(input("Введите операцию(степень это **): "))
        chisl2 = float(input("Введите 2 число: "))
    elif prot == None and prznak == None and prchis == None:
        chisl1 = float(input("Введите 1 число: "))
        znak = str(input("Введите операцию(степень это **): "))
        chisl2 = float(input("Введите 2 число: "))
    else:
        chisl1 = float(input("Введите 1 число: "))
        znak = str(input("Введите операцию(степень это **): "))
    prot = None
    prznak = None
    prchis = None
    exec("otvet = chisl1 {} chisl2".format(znak))
    print(chisl1, znak, chisl2, "=",  otvet)
    ot = str(input("Повторить операцию Enter, оставить ответ z, очистить o, в противном случае напишите что угодно: "))
    if ot == 'o':
        ot = ''
        continue
    elif ot == '':
        prot = otvet
        prznak = znak
        prchis = prchis + prchis
        ot = ''
        continue
    elif ot == 'z':
        prot = otvet
        prznak = znak
        ot = ''
        continue
    else:
        continue