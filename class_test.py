class Ball:
    def bounce(self):
        if self.direction == 'down':
            self.direction = 'up'
        elif self.direction == 'up':
            self.direction = 'down'

class TennisBall(Ball):
   def hit(self):
        if self.position == 'head':
           self.spin = 'Topspin'
        elif self.position == 'underneath':
            self.spin = 'Backspin'

myBall = Ball()
myBall.color = 'red'
myBall.size = 'big'
myBall.direction = 'down'
print myBall.__dict__

myBall2 = TennisBall()
myBall2.color='yellow'
myBall2.spin = None
myBall2.position = 'head'

print myBall2.__dict__
myBall2.hit()
print myBall2.__dict__

myBall2.position = 'underneath'
myBall2.hit()
print myBall2.__dict__

myBall2.direction = 'up'
myBall2.bounce()
print myBall2.__dict__
