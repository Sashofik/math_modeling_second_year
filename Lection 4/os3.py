import numpy as np
class ClassVector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __len__(self):
        vector = np.array([])
        return round(np.linalg.norm(vector))
        
    def __str__(self):
        return(str(self.x) + " " + str(self.y) + " " + str(self.z))

   #def __repr__(self):
   #    return print(self)
#
    def __add__(self, vect2):
        vector1 = np.array([self.x, self.y, self.z])
        vector2 = np.array([vect2.x, vect2.y, vect2.z])
        print(vector1 + vector2)

    def __sub__(self, vect2):
        vector1 = np.array([self.x, self.y, self.z])
        vector2 = np.array([vect2.x, vect2.y, vect2.z])
        print(vector1 - vector2)

    def __mul__(self, vect2):
        if type(vect2) == str:
            print("Нельзя так перемножать!")
        elif type(vect2) != ClassVector:
            print("Умножение на число: ")
            vector1 = np.array([self.x, self.y, self.z])
            print(np.dot(vector1, vect2))
        else:
            print("Умножение на вектор: ")
            vector1 = np.array([self.x, self.y, self.z])
            vector2 = np.array([vect2.x, vect2.y, vect2.z])
            print(vector1 * vector2)

    def __radd__(self, vect2):
        vect2 + self

    def __rsub__(self, vect2):
        vect2 - self

    def __rmul__(self, vect2):
        vect2 * self

    def __iadd__(self, vect2):
        vector1 = np.array([self.x, self.y, self.z])
        vector2 = np.array([vect2.x, vect2.y, vect2.z])
        vr = vector1 + vector2
        self.x = vr[0]
        self.y = vr[1]
        self.z = vr[2]
        return self

    def __isub__(self, vect2):
        vector1 = np.array([self.x, self.y, self.z])
        vector2 = np.array([vect2.x, vect2.y, vect2.z])
        vr = vector1 - vector2
        self.x = vr[0]
        self.y = vr[1]
        self.z = vr[2]
        return self

    def __imul__(self, vect2):
        vector1 = np.array([self.x, self.y, self.z])
        vector2 = np.array([vect2.x, vect2.y, vect2.z])
        vr = vector1 * vector2
        self.x = vr[0]
        self.y = vr[1]
        self.z = vr[2]
        return self 

    def __eq__(self, vect2):
        if self.x == vect2.x and self.y == vect2.y and self.z == vect2.z:
            print("Два вектора равны")
            return True
        else:
            print("Два вектора не равны")
            return False

    def __ne__(self, vect2):
        if self.x == vect2.x and self.y == vect2.y and self.z == vect2.z:
            print("Два вектора равны")
            return False
        else:
            print("Два вектора не равны")
            return True

    def __pow__(self, step):
        self.x = self.x ** step
        self.y = self.y ** step
        self.z = self.z ** step


vect1 = ClassVector(2, 4, 5)
vect2 = ClassVector(22, 44, 55)
print("Длина вектора: ", len(vect1))
print("--------------------------------------------------------------------------------------------")
print("Вектор: ", vect1)
#vect1
print("--------------------------------------------------------------------------------------------")
vect1 + vect2
print("--------------------------------------------------------------------------------------------")
vect1 - vect2
print("--------------------------------------------------------------------------------------------")
vect1 * 5
vect1 * vect2
#vect1 * "22"
print("--------------------------------------------------------------------------------------------")
print("Обратное: ")
vect2 + vect1
print("--------------------------------------------------------------------------------------------")
vect2 - vect1
print("--------------------------------------------------------------------------------------------")
vect2 * vect1
print("--------------------------------------------------------------------------------------------")
print("С i")
vect1 += vect2
print(vect1.x)
print(vect1.y)
print(vect1.z)
print("--------------------------------------------------------------------------------------------")
vect1 += vect2
print(vect1.x)
print(vect1.y)
print(vect1.z)
print("--------------------------------------------------------------------------------------------")
vect1 *= vect2
print(vect1.x)
print(vect1.y)
print(vect1.z)
print("--------------------------------------------------------------------------------------------")
vect1 != vect2
print("--------------------------------------------------------------------------------------------")
vect2 == vect2
print("--------------------------------------------------------------------------------------------")
vect2**4
print(vect2.x)
print(vect2.y)
print(vect2.z)