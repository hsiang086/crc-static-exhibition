import pygame
import os
import random
from math import sin, cos, pi, sqrt, pow


def init():
    global FPS
    global RES, WIDTH, HEIGHT 
    global clock
    global screen
    global x_center, y_center
    global third_scenes

    global aim


    RES = WIDTH, HEIGHT = 600, 600
    FPS = 60
    x_center, y_center = WIDTH / 2, HEIGHT / 2

    
    pygame.init()
    pygame.display.set_caption("third")
    screen = pygame.display.set_mode(RES)
    clock = pygame.time.Clock()

    third_scenes = pygame.sprite.Group()
    aim = Aim()
    third_scenes.add(Balloon(), aim)

class Aim(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill("green")
        self.rect = self.image.get_rect()
        self.speed = 5
        self.rect.centerx = x_center
        self.rect.centery = y_center
    def update(self):
        print(self.rect.center)
        key = pygame.key.get_pressed()
        if (key[pygame.K_w] or key[pygame.K_UP]) and 0 <= self.rect.center[1]:
            self.rect.centery -= self.speed
        if (key[pygame.K_s] or key[pygame.K_DOWN]) and self.rect.center[1] <= HEIGHT:
            self.rect.centery += self.speed
        if (key[pygame.K_a] or key[pygame.K_LEFT]) and 0 <= self.rect.center[0]:
            self.rect.centerx -= self.speed
        if (key[pygame.K_d] or key[pygame.K_RIGHT]) and self.rect.center[0] <= WIDTH:
            self.rect.centerx += self.speed

class Balloon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((80,80))
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.paused = False
        self.change = True
        self.theta = 0
        self.count = 0
        # circle radius
        self.movecircle_bool = True
        self.circle_speed = 2
        self.r = 150
        self.rect.centerx = x_center
        self.rect.centery = y_center
        self.circle_centerx = self.rect.centerx 
        self.circle_centery = self.rect.centery + self.r
        self.check = True
        # 
        self.movetriangle_bool = not self.movecircle_bool

    def circlemotion(self):
        theta_degree = self.theta * 2 * pi / 360
        costheta, sintheta = cos(theta_degree), sin(theta_degree)
        # rotation matrix   https://en.wikipedia.org/wiki/Rotation_matrix
        self.rect.centerx = self.circle_centerx - self.r * sintheta
        self.rect.centery = self.circle_centery - self.r * costheta
        if self.theta == 360:
            self.check = True

    def trianglemotion(self):
        m_x = sqrt(3)
        m_y = 1
        self.triangle_speed = 1
        self.step = 100
        self.count += 1
        
        if self.count == 3 * self.step:
            self.check = True
        self.count %= 3 * self.step
        if self.count < self.step and self.count > 0:
            self.rect.centerx += (m_x * self.triangle_speed)
            self.rect.centery += (m_y * self.triangle_speed)
        
        if self.count < 2 * self.step and self.count >= self.step:
            self.rect.centerx -= (sqrt(pow(m_x, 2) + pow(m_y,2))) * 2 * self.triangle_speed
            # self.rect.centery += m_y - m_y * speed
        
        if self.count < 3 * self.step and self.count >= 2 * self.step:
            self.rect.centerx += (m_x * self.triangle_speed)
            self.rect.centery -= (m_y * self.triangle_speed)
        
     
    
    def update(self):
        #if rotation_bool:
        #    self.rotate_init()
        #    rotation_bool = False
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.paused = not self.paused
                    if self.paused:
                        print("paused")
                if event.key == pygame.K_m:
                    self.check = True
                if event.key == pygame.K_SPACE and self.rect.collidepoint(aim.rect.center):
                    self.change = not self.change
                    if self.change:
                        self.image.fill("blue")
                    else:
                        self.image.fill("pink")
                    

        
        if self.check:
            rand_num = random.randint(0,1)
            if rand_num == 0:
                self.movecircle_bool = True
                self.circle_centerx = self.rect.centerx - self.r
                self.circle_centery = self.rect.centery
            else :
                self.movecircle_bool = False
            self.movetriangle_bool = True if rand_num == 1 else False
            self.check = False
        if not self.paused:
            if self.movecircle_bool:
                self.theta += self.circle_speed
                self.circlemotion()
            if self.movetriangle_bool:
                self.trianglemotion()
            self.theta %= 360
        

init()

while True:
    screen.fill("black")
    third_scenes.draw(screen)
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            os._exit(True)

    third_scenes.update()
    pygame.display.update()