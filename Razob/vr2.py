class Ball:

    def __init__(self, mass):
        print('Я вызвался')

        self.mass = mass
        self.image = 'hexagone'
        self.x = 0
        self.y = 0
        self.state = True

    def drop(self):
        if self.state:
            print('Я подбросился')
            self.x = 2
        else:
            print("Я проколот")

    def kick(self):
        print('Я пнулся')
        self.x += 1

    def fail(self):
        self.state = False

# Вызов полей
#print(Ball.color)
#print(Ball.image)

ball = Ball(0.5)
print(ball.image)
print(ball.mass)
ball.image = 'lines'
print(ball.image)

print(ball.x)
ball.drop()
print(ball.x)
ball.drop()
print(ball.x)
ball.kick()
ball.fail()
print(ball.x)
ball.kick()
print(ball.x)