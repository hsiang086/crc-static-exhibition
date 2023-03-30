import pygame
import random

def init():
    global FPS
    global RES, WIDTH, HIGHT
    global clock
    global screen
    global POS

    FPS = 60
    RES = WIDTH, HIGHT = (1600, 900)

    POS=[(HIGHT/2)-200,(HIGHT/2),(HIGHT/2)+200]

    clock = pygame.time.Clock()
    
    itv = 0
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
        self.rect.x = 10
        self.rect.centery = HIGHT/2
        self.pos = 1
        self.itv = 0
         
    def update(self):
        self.itv += 1
        key_pressed = pygame.key.get_pressed()
        if self.itv >= 8:
            if key_pressed[pygame.K_UP]:
                if self.pos == 0:
                    self.pos = 0
                else:
                    self.pos -= 1 
            if key_pressed[pygame.K_DOWN]:
                if self.pos == 2:
                    self.pos = 2
                else:
                    self.pos += 1     
            self.itv = 0
        self.rect.centery = POS[self.pos]         

class Object(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill((0,153,153))
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH
        self.pos = random.randrange(0,3)
        self.rect.centery = POS[self.pos]
        self.v = -5
        self.itv = 0
    def update(self):
        if self.rect.right >= 0:
            self.rect.x += self.v
        else:    
            self.kill()



        
        
all_sprites = pygame.sprite.Group()
objects = pygame.sprite.Group() 
player = Player()
all_sprites.add(player) 


time = 0
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if time >= 90:
        Obj = Object()
        all_sprites.add(Obj)
        objects.add(Obj)  
        time = 0

    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, objects, 0)
    if hits:
        running = False
    screen.fill((255,255,255))
    all_sprites.draw(screen)
    pygame.display.update()
    time += 1        

pygame.quit()