class Pyramid:
    def __init__(self, max_h):
        self.max_h = max_h
        self.bricks_count = 0
        self.ur = max_h
        self.col = 1
        
    def add_bricks(self, kir):
        self.ur = self.ur - kir
        if self.col == (self.max_h-1):
            if self.ur == 0:
                self.bricks_count += kir
                self.ur = self.max_h - self.col
                print("Пирамида построенна!!!")
                self.is_done()
                exit(0)
            if self.ur < 0:
                print("Пирамида разрушенна!!!")
                exit(0)
        self.bricks_count += kir
        if self.ur == 0:
            self.ur = self.max_h - self.col
            self.col += 1
        if self.ur < 0:
            self.ur = self.max_h - self.col - self.ur
            self.col += 1
        
    def get_height(self):
        print("Текущая высота пирамиды:", (self.max_h - self.col + 1))

    def is_done(self):
        kirvsego = self.max_h * (self.max_h + 1) / 2
        print("Процентная готовность пирамиды:", self.bricks_count / kirvsego * 100, "%")


class Builder:
    def __init__(self, bricks):
        self.bricks =  bricks
        self.my_pyramid = Pyramid(15)
        self.day = 1
        
    def buy_bricks(self):
        self.bricks += (15 - self.bricks)

    def build_pyramyd(self):
        if (self.my_pyramid.ur % 5) == 0:
            self.my_pyramid.add_bricks(5)
            kolkir = 5
        elif (self.my_pyramid.ur % 4) == 0:
            self.my_pyramid.add_bricks(4)
            kolkir = 4
        elif (self.my_pyramid.ur % 3) == 0:
            self.my_pyramid.add_bricks(3)
            kolkir = 3
        elif (self.my_pyramid.ur % 2) == 0:
            self.my_pyramid.add_bricks(2)
            kolkir = 2
        else:
            self.my_pyramid.add_bricks(1)
            kolkir = 1
        if self.bricks >= kolkir:
            self.bricks = self.bricks - kolkir
        else:
            self.buy_bricks()
            self.bricks = self.bricks - kolkir
        print("Кирпичей сегодня положенно:", kolkir)

    def work_day(self):
        self.build_pyramyd()
        print("День ", self.day)

        print("Количество кирпичей у строителя:", self.bricks)
        self.my_pyramid.is_done()
        self.day += 1

b = Builder(13)

while True:
    b.work_day()