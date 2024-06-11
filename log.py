from game_object import GameObject
class Log(GameObject):
    def __init__(self,x,y,width,height,color,direction,speed):
        super(). __init__(x,y,width,height,color)
        self.direction = direction
        self.speed = speed

    def move(self):
        if self.direction == "left":
            self.x -= self.speed
        else:
            self.x += self.speed

        if self.x <= 0:
            self.direction = "right"

        elif self.x >= 1000 - self.width:
            self.direction = "left"