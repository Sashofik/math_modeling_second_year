class Ball(object):
    R = 6
    def __init__(self, col):
        self.col = col

    def prin(self):
        print(self.col)
        print(Ball.R)

    def initiat(self):
        print("Инициирую вывод параметров...")
        self.prin()

ball_1 = Ball('red')
#print(ball_1.prin())
ball_1.R = 12
ball_1.initiat()
#print(ball_1.R)
#print(Ball.R)
#Ball.R = 44
#new_ball = Ball("blue")
#print(new_ball.R)

