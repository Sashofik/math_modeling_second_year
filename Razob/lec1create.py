class Method:
    R = 6
    def __init__(self, col):
        self.col = col
        self.x = 0
        self.y = 0

    def prin(self):
        print(self.col)
        print(self.R)

    def initiat(self):
        print("Инициирую вывод параметров...")
        self.prin()

ball_1 = Method('red')
#print(ball_1.prin())
ball_1.R = 12
ball_1.initiat()
#print(ball_1.R)
#print(Ball.R)
#Ball.R = 44
#new_ball = Ball("blue")
#print(new_ball.R)

