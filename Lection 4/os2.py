class Orgclet:
    def __init__(self, colvo):
        self.colvo = colvo

    def __add__(self, clet2):
        print(self.colvo + clet2.colvo)

    def __sub__(self, clet2):
        print(self.colvo - clet2.colvo)

    def __mul__(self, clet2):
        print(self.colvo * clet2.colvo)

    def __truediv__(self, clet2):
        print(int(self.colvo / clet2.colvo))

clet1 = Orgclet(363)
clet2 = Orgclet(128)

clet1 + clet2
print("--------------------------------------------------------------------------------------------")
clet1 - clet2
print("--------------------------------------------------------------------------------------------")
clet1 * clet2
print("--------------------------------------------------------------------------------------------")
clet1 / clet2