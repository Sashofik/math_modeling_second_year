class Tomato:
    states = ["Отсутствует", "Цветение", "Зеленый", "Красный"]
    def __init__(self, index):
        self.index = index
        self.soz = 0
        self.state = self.states[self.soz]
        
    
    def grow(self):
        self.soz += 1
        self.state = self.states[self.soz]

    def is_ripe(self):
        if self.soz == len(self.states):
            return(True)
    
class TomatoBush:
    def __init__(self, kolvo):
        self.kolvo = kolvo
        self.tomatoes = []
        for i in range(kolvo):
            exec('self.tomato' + str(i)) = Tomato(i)
        for i in range(kolvo):
            exec("self.tomatoes.append('{}')".format("tomato" + str(i)))

    def grow_all(self):
        for i in range(self.kolvo):
            exec("self.tomato{}.grow".format(str(i)))
        
    def all_are_ripe(self):
        a = 1
        for i in range(self.kolvo):
            exec("if self.tomato{}.is_ripe != True: a = 0".format(str(i)))
            if a == 1:
                return(True)

    def give_away_all(self):
        self.tomatoes = []
        for i in range(kolvo):
            exec("del self.tomato{}".format(str(i)))
        
class Gardener:
    def __init__(self, name):
        self.name = name
        self.plant = TomatoBush(15)
    
    def work(self):
        self.plant.grow_all()

    def harvest(self):
        if self.plant.all_are_ripe() == True:
            self.plant.give_away_all()
            print("Урожай собран")
            exit(0)
        else:
            print("Не все плоды созрели")
            self.work()

 #   def knowledge_base(self):

g = Gardener("Вася")

while True:
    g.harvest()