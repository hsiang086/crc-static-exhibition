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
        if not pause: self.rect.centery = POS[self.pos]
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
    def collide(self):
        effect = collide_effect(self.rect.right, self.rect.centery)
        all_sprites.add(effect)      


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
        if not pause:
            if self.rect.right >= 0:
                self.rect.x += self.v
            else:    
                self.kill()

class collide_effect(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((75,75))
        self.image.fill((153,153,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
    def update(self):
        if not pause:
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
p_moment = 0 
t_pause = 3 #Stop for __ second if collide
object_generate_interval = 2 #(seconds)
ogi = object_generate_interval*FPS

pause = False
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not pause:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player.UP()
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.DOWN()
    if time >= ogi:
        Obj = Object()
        all_sprites.add(Obj)
        objects.add(Obj)  
        time = 0
    t_run = tm.time()
    
    if pause:
        if tm.time()-p_moment >= t_pause:
            pause = False

    all_sprites.update()


    hits = pygame.sprite.spritecollide(player, objects, 1)
    screen.fill((255,255,255))
    timerunning.display(t_run)
    all_sprites.draw(screen)
    if hits:
        pause = True
        p_moment = tm.time()
        player.collide()
        
    
    pygame.display.update()

    time += 1        

pygame.quit()