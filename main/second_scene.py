import pygame
import random
import time as tm
import os

def init():
    global FPS
    global RES, WIDTH, HIGHT, Road_Width
    global clock
    global screen
    global POS
    global pause_times, time_start
    global object_kill
    global speed
    global tree_pos
    global pause

    tree_pos = 125
    object_kill = False
    pause_times = 0
    time_start = tm.time()
    FPS = 60
    RES = WIDTH, HIGHT = (1920,1080)
    Road_Width = 230
    POS=[(HIGHT/2)-Road_Width-50,(HIGHT/2)-30,(HIGHT/2)+Road_Width-10]
    speed = -40
    clock = pygame.time.Clock()
    
    itv = 0
    pygame.init()

    screen = pygame.display.set_mode(RES)
    

    pygame.display.set_caption("second scene")

init()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/second_scene/分鏡1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.centery = HIGHT/2
        self.pos = 1
        self.time =1

    def update(self):
        global pause
        if not pause: 
            self.rect.centery = POS[self.pos]
            self.time += 1/4
            if self.time % 3 ==0:
                self.image = pygame.image.load("images/second_scene/分鏡1.png").convert_alpha()
            elif self.time %3 ==1:
                self.image = pygame.image.load("images/second_scene/分鏡2.png").convert_alpha()
            elif self.time %3 ==2:
                self.image = pygame.image.load("images/second_scene/分鏡3.png").convert_alpha()
        else:
            self.image = pygame.image.load("images/second_scene/撞擊.png").convert_alpha()
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
        self.imagerandom = random.randint(0,2)
        print(self.imagerandom)
        if self.imagerandom == 0:
            self.image = pygame.image.load("images/second_scene/障礙物1 去背.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (200, 200))
        elif self.imagerandom == 1:
            self.image = pygame.image.load("images/second_scene/障礙物2 去背.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (200, 200))
        elif self.imagerandom == 2:
            self.image = pygame.image.load("images/second_scene/障礙物3 去背.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH
        self.pos = random.randrange(0,3)
        self.rect.centery = POS[self.pos]
        self.v = speed
    def update(self):
        if not pause:
            if self.rect.right >= 0:
                self.rect.x += self.v
            else:    
                self.kill()


class BalloonAppear(pygame.sprite.Sprite):
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("images/third_scene/balloon_red.png")).convert_alpha()
        # self.image = pygame.transform.scale(self.image, (700, 700))
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH
        self.rect.centery = HIGHT / 2
        self.v = speed
    def update(self):
        if not pause:
            self.rect.centerx += self.v

class collide_effect(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/second_scene/撞擊特效.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
    def update(self):
        if not pause:
            self.kill()    

class Wallpaper(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/second_scene/road.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, RES)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HIGHT / 2
        self.speed = speed

    def update(self):
        if wallpapercontinue.rect.centerx <= WIDTH / 2:
            self.rect.left = wallpapercontinue.rect.right
        self.rect.centerx += self.speed
wallpaper = Wallpaper()
class WallpaperContinue(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/second_scene/road.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, RES)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.left = wallpaper.rect.right
        self.speed = speed

    def update(self):
        if wallpaper.rect.centerx <= WIDTH / 2:
            self.rect.left = wallpaper.rect.right
        self.rect.centerx += self.speed

wallpapercontinue = WallpaperContinue()

class TimeRunning():
    def __init__(self):
        self.time = 60
        self.time_start = tm.time()
        self.text_rect = (WIDTH / 2, 100)
    def display(self,time_run):
        time_left = self.time - int(time_run - self.time_start)
        if time_left < 0:
            init()
            run()
            global running
            running = False
        font = pygame.font.SysFont('Arial', 150, bold = True)
        text = font.render(str(time_left), True, 'black')
        screen.blit(text, self.text_rect)
global timerunning
timerunning = TimeRunning()
timerunning.__init__()

class TB(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/second_scene/time background.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(400, 500))
        self.rect = self.image.get_rect()
        self.rect.top = -60
        self.rect.centerx = WIDTH / 2 + 72


def run():
    global tb
    global pause
    global all_sprites
    global timerunning
    global running
    timerunning.__init__()
    time_start = tm.time()
    tb = TB()

    all_sprites = pygame.sprite.Group()
    objects = pygame.sprite.Group() 
    balloon = pygame.sprite.Group()

    all_sprites.add(wallpaper,wallpapercontinue,tb)
    player = Player()
    all_sprites.add(player) 


    o_time = 0
    tree_time = 0
    up_down = 0 

    p_moment = 0 
    t_pause = 3 #Stop for __ second if collide
    tree_generate_interval = 1.5
    object_generate_interval = 2 #(seconds)
    ogi = object_generate_interval*FPS
    tgi = tree_generate_interval*FPS

    pause = False
    running = True
    object_kill = False
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
        if o_time >= ogi and not object_kill:
            Obj = Object()
            all_sprites.add(Obj)
            objects.add(Obj)  
            o_time = 0
        t_run = tm.time()
        
        if pause:
            if tm.time()-p_moment >= t_pause:
                pause = False



        hits = pygame.sprite.spritecollide(player, objects, 1)
        screen.fill((255,255,255))
        global pause_times
        if hits:
            pause = True
            p_moment = tm.time()
            player.collide()
            pause_times += 1
        if tm.time()-time_start >= 30 + pause_times*3 and not object_kill:
            balloon_appear = BalloonAppear()
            object_kill = True
            balloon.add(balloon_appear)
            all_sprites.add(balloon_appear)
        balloon_hits = pygame.sprite.spritecollide(player, balloon, 1)
        if balloon_hits:
            running = False
        if not pause:
            all_sprites.update()
        all_sprites.draw(screen)
        timerunning.display(t_run)
        
        pygame.display.update()
        if not pause:
            o_time += 5        
            tree_time += 1

