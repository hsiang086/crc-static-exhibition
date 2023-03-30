import pygame
from time import sleep
import random

def init():
    global FPS
    global RES, WIDTH, HIGHT
    global clock
    global screen

    FPS = 60
    RES = WIDTH, HIGHT = (1200, 700)
    clock = pygame.time.Clock()
    
    pygame.init()
    screen = pygame.display.set_mode(RES)
    

    pygame.display.set_caption("second scene")

init()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100,100))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.centery = HIGHT / 2
        self.position = 0
        # self.pos = 0
        # self.itv = 0
         
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if self.rect.centery > HIGHT / 2 - 200 :
                        self.position -= 1
                if event.key == pygame.K_s:
                    if self.rect.centery < HIGHT / 2 + 200 :
                        self.position += 1
        self.rect.centery += self.position * 200
        self.position = 0
        # self.itv += 1
        # key_pressed = pygame.key.get_pressed()
        # if self.itv >= 8:
        #     if key_pressed[pygame.K_UP] or key_pressed[pygame.K_w]:
        #         if self.pos == -1:
        #             self.pos = -1
        #         else:
        #             self.pos -= 1
        #         while self.rect.centery > (HIGHT / 2) + self.pos * 200:
        #             self.rect.centery -= 2 
        #     if key_pressed[pygame.K_DOWN] or key_pressed[pygame.K_s]:
        #         if self.pos == 1:
        #             self.pos = 1
        #         else:
        #             self.pos += 1
        #         self.rect.centery = (HIGHT / 2) + self.pos * 200      
        #     self.itv = 0     

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100,100))
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.centery = ( HIGHT / 2 ) + ( 200 * ( random.randint(-1, 1) ) )
        self.rect.centerx = 0#WIDTH + 10

    

        
all_sprites = pygame.sprite.Group()
player = Player()
obstacle = Obstacle()
all_sprites.add(player, obstacle) 


running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
           
    all_sprites.update()   
    screen.fill((255,255,255))
    all_sprites.draw(screen)
    pygame.display.update()        

pygame.quit()