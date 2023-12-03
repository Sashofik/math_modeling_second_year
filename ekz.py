tren = [5, 10, 15, 20, 40, 50, 55]
file = open("outpyt9.txt", "w")

for i in tren:
    prop = 200
    for j in range(i):
            if prop != 400:
                    prop += 5
    print("На", i, "тренировоке проплывается",  prop, "м")
    file.write(str(prop) + "\n")
    
file.close()