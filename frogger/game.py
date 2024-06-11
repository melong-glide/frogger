import pygame
from frog import Frog
from obstacle import Obstacle
from game_object import GameObject
class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1000,1000))
        self.frog = Frog(100,950,50,50,50, (50, 168, 82))
        self.obstacle1 = Obstacle(496,600,100,50,7, "left", (227, 86, 86))
        self.obstacle2 = Obstacle(134,700,100,50,4, "right", (80, 222, 108))
        self.obstacle3 = Obstacle(345,800,100,50,8, "left", (235, 124, 68))
        self.starting_zone = GameObject(0, 900, 1000, 100, (125, 117, 114))
        self.safe_zone = GameObject(0, 500, 1000, 100, (125, 117, 114))
        self.water = Obstacle(0,0, 1000, 500, 0, "left", (69, 141, 196))
        self.goal1 = GameObject(0,0,150,150, (255, 255, 0))
        self.goal2 = GameObject(300,0,150,150, (255, 255, 0))
        self.goal3 = GameObject(500,0,150,150, (255, 255, 0))
        self.goal4 = GameObject(1000-150,0,150,150, (255, 255, 0))
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.game_loop()




    def event_handler(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.frog.x += self.frog.speed
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.frog.x -= self.frog.speed
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.frog.y -= self.frog.speed
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.frog.y += self.frog.speed
    

    def game_loop(self):
        while True:
            self.clock.tick(self.fps)
            self.event_handler()
            self.frog.update()
            self.obstacle1.move()
            self.obstacle2.move()
            self.obstacle3.move()
            self.obstacle1.update()
            self.obstacle2.update()
            self.obstacle3.update()

            self.draw()
            pygame.display.update()

    def draw(self):
        self.window.fill((0,0,0))
        self.starting_zone.draw(self.window)
        self.water.draw(self.window)
        self.goal1.draw(self.window)
        self.goal2.draw(self.window)
        self.goal3.draw(self.window)
        self.goal4.draw(self.window)
        self.safe_zone.draw(self.window)
        self.frog.draw(self.window)
        self.obstacle1.draw(self.window)
        self.obstacle2.draw(self.window)
        self.obstacle3.draw(self.window)
        

        pygame.display.update()


