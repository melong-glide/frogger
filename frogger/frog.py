from game_object import GameObject

class Frog(GameObject):
    def __init__(self, x,y,width,height,speed, color):
        super(). __init__(x,y,width,height, color)
        self.speed = speed




