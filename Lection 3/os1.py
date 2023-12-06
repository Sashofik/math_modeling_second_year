import numpy as np

class Human:
    default_name = 'Sasha'
    default_age = 17
    def __init__(self, money, house):
        self.name = self.default_name
        self.age = self.default_age
        self._money = money
        self._house = house

    # Метод экземпляра класса
    def info(self):
        print("Имя: ", self.name)
        print("Возраст: ", self.age)
        print("Деньги: ", self._money)
        print("Дом: ", self._house)

    def default_info():
        print("Имя по умолчанию: ", Human.default_name)
        print("Возраст по умолчанию: ", Human.default_age)

    def _make_deal(self, house, price):
        self._money -= price
        self._house.append(house)
    
    def earn_money(self, mon):
        self._money += mon
    
    def buy_house(self, house, discond):
        if house.final_price(discond) > self._money:
            print("Нужно больше золота")
        else:
            self._make_deal(house, house.final_price(discond))

class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price
        
    def final_price(self, discond):
        return self._price-discond

class SmallHouse(House):
    def __init__(self, price):
        super().__init__(area = 40, price=price)


Human.default_info()
print("--------------------------------------------------------------------------------------------")

firstpeople = Human(780, [])

firstpeople.info()
print("--------------------------------------------------------------------------------------------")

thirdhouse = SmallHouse(350)

firsthouse = House(120, 900)
secondhouse = House(400, 3000)


hhhouse1 = House(100, 300)
hhhouse2 = House(450, 2250)

secondpeople = Human(5000, [hhhouse2])
thirdpeople = Human(100, [hhhouse1])

thirdpeople.buy_house(thirdhouse, 100)
print("--------------------------------------------------------------------------------------------")
thirdpeople.earn_money(400)
thirdpeople.buy_house(thirdhouse, 100)
thirdpeople.info()