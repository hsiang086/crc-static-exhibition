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

    RES = WIDTH, HEIGHT = 600, 600
    FPS = 60
    x_center, y_center = WIDTH / 2, HEIGHT / 2
    theta = 0
    
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
        self.r = 2
        self.rect.centerx = x_center
        self.rect.centery = y_center
    def movecircle(self):
        theta_degree = theta * 2 * pi / 360
        self.rect.centerx += self.r * cos(theta_degree)
        self.rect.centery += self.r * sin(theta_degree)
    def update(self):
        self.movecircle()

init()
while True:
    theta += 1
    theta %= 360
    screen.fill("black")
    third_scenes.draw(screen)
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            os._exit(True)
    third_scenes.update()
    pygame.display.update()