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
        self.r = 130
        self.rect.centerx = x_center
        self.rect.centery = y_center
        self.circle_centerx = self.rect.centerx 
        self.circle_centery = self.rect.centery + self.r
        self.check = True
        self.bf_x = self.rect.centerx
        self.bf_y = self.rect.centery
        # 
        self.movetriangle_bool = not self.movecircle_bool

    def circlemotion(self):
        theta_degree = self.theta * 2 * pi / 360
        costheta, sintheta = cos(theta_degree), sin(theta_degree)
        # rotation matrix   https://en.wikipedia.org/wiki/Rotation_matrix
        self.rect.centerx = self.circle_centerx + self.r * sintheta
        self.rect.centery = self.circle_centery - self.r * costheta
        if self.theta == 360:
            self.check = True

    def trianglemotion(self):
        m_x = 1
        m_y = sqrt(3)
        bf_bool = True
        

        self.triangle_speed = 1.5
        self.step = 100
        self.count += 1
        
        if self.count == 3 * self.step:
            self.rect.centerx = int(self.bf_x) + 1
            self.rect.centery = int(self.bf_y) + 2
            bf_bool = False
            self.check = True

        self.count %= 3 * self.step
        if self.count < self.step and self.count > 0:
            self.bf_x += m_x * self.triangle_speed
            self.bf_y += m_y * self.triangle_speed
        
        if self.count < 2 * self.step and self.count >= self.step:
            self.bf_x -= sqrt(pow(m_x, 2) + pow(m_y,2)) * self.triangle_speed
            # self.rect.centery += m_y - m_y * speed
        
        if self.count < 3 * self.step and self.count >= 2 * self.step:
            self.bf_x += m_x * self.triangle_speed
            self.bf_y -= m_y * self.triangle_speed

        if bf_bool:
            self.rect.centerx = self.bf_x
            self.rect.centery = self.bf_y
            
     
    
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
                self.circle_centerx = self.rect.centerx 
                self.circle_centery = self.rect.centery + self.r
            else :
                self.movecircle_bool = False
            if rand_num == 1:
                self.movetriangle_bool = True
                self.bf_x = self.rect.centerx
                self.bf_y = self.rect.centery
            else :
                self.movetriangle_bool = False
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