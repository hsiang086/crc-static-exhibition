import pygame

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
        self.pos = 0
        self.itv = 0
         
    def update(self):
        self.itv += 1
        key_pressed = pygame.key.get_pressed()
        if self.itv >= 8:
            if key_pressed[pygame.K_UP]:
                if self.pos == -1:
                    self.pos = -1
                else:
                    self.pos -= 1
                while self.rect.centery >= (HIGHT/2) + self.pos*200:
                    self.rect.centery -= 2 
            if key_pressed[pygame.K_DOWN]:
                if self.pos == 1:
                    self.pos = 1
                else:
                    self.pos += 1
                self.rect.centery = (HIGHT/2) + self.pos*200      
            self.itv = 0     

        
        
all_sprites = pygame.sprite.Group()
objects = pygame.sprite.Group() 
player = Player()
obstacle = Obstacle()
all_sprites.add(player, obstacle) 


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