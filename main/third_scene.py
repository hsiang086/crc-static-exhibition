import pygame
import os
from math import sin, cos, pi

def init():
    global FPS
    global RES, WIDTH, HEIGHT 
    global clock
    global screen
    global x_center, y_center
    global third_scenes
    global theta
    global movecircle_bool
    global circle_move_speed
    global key

    RES = WIDTH, HEIGHT = 600, 600
    FPS = 60
    x_center, y_center = WIDTH / 2, HEIGHT / 2

    theta = 0
    circle_move_speed = 2
    movecircle_bool = False
    
    pygame.init()
    pygame.display.set_caption("third")
    screen = pygame.display.set_mode(RES)
    clock = pygame.time.Clock()

    third_scenes = pygame.sprite.Group()
    third_scenes.add(Balloon(),Aim())

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
        key= pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.rect.centerx -= self.speed
        if key[pygame.K_d]:
            self.rect.centerx += self.speed
        if key[pygame.K_w]:
            self.rect.centery -= self.speed
        if key[pygame.K_s]:
            self.rect.centery += self.speed

class Balloon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((80,80))
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.speed = 5
        # circle radius
        self.r = 100
        self.rect.centerx = x_center
        self.rect.centery = y_center
        self.circle_centerx = self.rect.centerx - self.r
        self.circle_centery = self.rect.centery

    def circlemotion(self):
        theta_degree = theta * 2 * pi / 360
        costheta, sintheta = cos(theta_degree), sin(theta_degree)
        # rotation matrix   https://en.wikipedia.org/wiki/Rotation_matrix
        self.rect.centerx = self.circle_centerx + self.r * costheta
        self.rect.centery = self.circle_centery + self.r * sintheta
    
    def update(self):
        #if rotation_bool:
        #    self.rotate_init()
        #    rotation_bool = False
        if movecircle_bool:
            self.circlemotion()
        

init()
paused = True
while True:

    screen.fill("black")
    third_scenes.draw(screen)
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            os._exit(True)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
                if not paused:
                    print("paused")
    movecircle_bool = True
    if paused:    
        if movecircle_bool:
            theta += circle_move_speed
            theta %= 360
        third_scenes.update()
        pygame.display.update()