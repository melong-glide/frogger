import pygame
from frog import Frog
from obstacle import Obstacle
from game_object import GameObject
from log import Log
from fly import Fly
import random

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
        self.goal1 = GameObject(0,0,150,200, (255, 255, 0))
        self.goal2 = GameObject(300,0,150,200, (255, 255, 0))
        self.goal3 = GameObject(600,0,150,200, (255, 255, 0))
        self.goal4 = GameObject(1000-150,0,150,200, (255, 255, 0))
        self.log1 = Log(200,200,200,50,(135, 62, 35), "right", 3)
        self.log2 = Log(200,250,200,50,(135, 62, 35), "right", 2)
        self.log3 = Log(200,300,200,50,(135, 62, 35), "right", 5)
        self.log4 = Log(200,350,200,50,(135, 62, 35), "right", 4)
        self.log5 = Log(200,400,200,50,(135, 62, 35), "right", 3.4)
        self.log6 = Log(200,450,200,50,(135, 62, 35), "right", 2.7)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.death = False
        self.fly = Fly(50,50, 50, 50, (28, 28, 27))
        self.locked_flys = []
        self.goal_positions = [(50,50), (350, 50),(650,50), (900,50)]
        self.spawn_event  =  pygame.event.custom_type()
        pygame.time.set_timer(self.spawn_event, random.randint(2000, 10000), 1)
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
            if event.type == self.spawn_event:
                self.spawn_fly()
                pygame.time.set_timer(self.spawn_event, random.randint(2000, 10000), 1)

            if event.type == pygame.MOUSEMOTION:
                print(event.pos)
    

    def game_loop(self):
        while True:
            self.clock.tick(self.fps)
            self.event_handler()
            self.frog.update()
            self.obstacle1.move()
            self.obstacle2.move()
            self.obstacle3.move()
            self.log1.move()
            self.log2.move()
            self.log3.move()
            self.log4.move()
            self.log5.move()
            self.log6.move()
            self.obstacle1.update()
            self.obstacle2.update()
            self.obstacle3.update()
            self.check_game_over()
            self.log1.update()
            self.log2.update()
            self.log3.update()
            self.log4.update()
            self.log5.update()
            self.log6.update()
            self.check_on_log()
            self.check_fly()
            self.fly.update()
            self.draw()
            pygame.display.update()

    def draw(self):
        self.window.fill((0,0,0))
        self.starting_zone.draw(self.window)
        self.water.draw(self.window)
        self.log1.draw(self.window)
        self.log2.draw(self.window)
        self.log3.draw(self.window)
        self.log4.draw(self.window)
        self.log5.draw(self.window)
        self.log6.draw(self.window)
        self.goal1.draw(self.window)
        self.goal2.draw(self.window)
        self.goal3.draw(self.window)
        self.goal4.draw(self.window)
        self.safe_zone.draw(self.window)
        self.frog.draw(self.window)
        self.obstacle1.draw(self.window)
        self.obstacle2.draw(self.window)
        self.obstacle3.draw(self.window)
        self.fly.draw(self.window)
        for fly in self.locked_flys:
            fly.draw(self.window)

        pygame.display.update()

    def check_game_over(self):
        if self.obstacle1.rect.colliderect(self.frog.rect) or self.obstacle2.rect.colliderect(self.frog.rect) or self.obstacle3.rect.colliderect(self.frog.rect):
            death = True
        elif self.water.rect.colliderect(self.frog.rect) and (not self.log1.rect.colliderect(self.frog.rect) and not self.log2.rect.colliderect(self.frog.rect) and not self.log3.rect.colliderect(self.frog.rect)  and not self.log4.rect.colliderect(self.frog.rect)  and not self.log5.rect.colliderect(self.frog.rect) and not self.log6.rect.colliderect(self.frog.rect) and not self.goal1.rect.colliderect(self.frog.rect) and not self.goal2.rect.colliderect(self.frog.rect) and not self.goal3.rect.colliderect(self.frog.rect) and not self.goal4.rect.colliderect(self.frog.rect)):
            death = True
        else:
            death = False

        
        if death == True:
            pygame.quit()
            quit()

    def check_on_log(self):
        on = False
        if self.log1.rect.colliderect(self.frog.rect):
            log_speed = self.log1.speed
            log_direction = self.log1.direction
            on = True

        elif self.log2.rect.colliderect(self.frog.rect):
            log_speed = self.log2.speed
            log_direction = self.log2.direction
            on = True
        elif self.log3.rect.colliderect(self.frog.rect):
            log_speed = self.log3.speed
            log_direction = self.log3.direction
            on = True
        elif self.log4.rect.colliderect(self.frog.rect):
            log_speed = self.log4.speed
            log_direction = self.log4.direction
            on = True
        elif self.log5.rect.colliderect(self.frog.rect):
            log_speed = self.log5.speed
            log_direction = self.log5.direction
            on = True
        elif self.log6.rect.colliderect(self.frog.rect):
            log_speed = self.log6.speed
            log_direction = self.log6.direction
            on = True

        if on == True:
            if log_direction == "right":
                self.frog.x += log_speed
            else:
                self.frog.x -= log_speed

    def spawn_fly(self):
        self.fly_position = random.choice(self.goal_positions)
        self.fly.x = self.fly_position[0]
        self.fly.y = self.fly_position[1]
        
    def check_fly(self):
        if self.fly.rect.colliderect(self.frog.rect):
            position = (self.fly.x, self.fly.y)
            self.goal_positions.remove(position)
            self.fly.locked = True
            self.fly.color = (245, 66, 66)
            self.locked_flys.append(self.fly)
            self.fly = Fly(50,50, 50, 50, (28, 28, 27))
            self.spawn_fly()

        
        
        

        
            

            



