list1 = [23, 96, 53, 45, 9, 25, 80, 13, 79, 52]
list2 = list(map(lambda a: a**3 if a%2==0 else a, list1))
print(list2)