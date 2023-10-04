class Tomato:
    states = ["Отсутствует", "Цветение", "Зеленый", "Красный"]
    def __init__(self, index):
        self.index = index
        self.state = self.states[0]
        self.col = 1
    
    def grow(self):
        
    def is_ripe(self):
        
    
class TomatoBush:
    def __init__(self, kolvo):
        self.kolvo = kolvo
        for i in range(kolvo):
            globals()['tomato' + str(i)] = Tomato(i))
        for i in range(kolvo):
            exec("self.tomatoes.append = {}".format('tomato' + str(i)))

    def grow_all(self):
        
    def all_are_ripe(self):

    def give_away_all(self):

class Gardener:
    def __init__(self, name):
        self.name = name
        self.plant = TomatoBush(15)
    
    def work(self):
        
    def harvest(self):

    def knowledge_base(self):