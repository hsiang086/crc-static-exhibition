import pygame
import random
import time as tm

def init():
    global FPS
    global RES, WIDTH, HIGHT
    global clock
    global screen
    global POS
 

    FPS = 60
    RES = WIDTH, HIGHT = (1500, 800)
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
        """self.itv += 1
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
            self.itv = 0"""
        self.rect.centery = POS[self.pos]
    def UP(self):
        if self.pos == 0:
            self.pos = 0
        else:
            self.pos -= 1
    def DOWN(self):
        if self.pos == 2:
            self.pos = 2
        else:
            self.pos += 1


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


class TimeRunning():
    def __init__(self):
        self.time = 60
        self.time_start = tm.time()
        self.text_rect = (WIDTH / 2, 100)
    def display(self,time_run):
        time_left = self.time - int(time_run - self.time_start)
        if time_left < 0:
            global running
            running = False
        font = pygame.font.SysFont('Arial', 70, bold = True)
        text = font.render(str(time_left), True, 'black')
        screen.blit(text, self.text_rect)


global timerunning
timerunning = TimeRunning()
timerunning.__init__()
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player.UP()
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.DOWN()
    if time >= 60:
        Obj = Object()
        all_sprites.add(Obj)
        objects.add(Obj)  
        time = 0
    t_run = tm.time()
    
    
    all_sprites.update()


    hits = pygame.sprite.spritecollide(player, objects, 0)
    screen.fill((255,255,255))
    timerunning.display(t_run)
    all_sprites.draw(screen)
    if not hits :
        pygame.display.update()

    time += 1        

pygame.quit()