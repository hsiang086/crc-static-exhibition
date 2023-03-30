import pygame

def init():
    global FPS
    global RES, WIDTH, HIGHT
    global clock
    global screen

    FPS = 60
    RES = WIDTH, HIGHT = (1200, 700)
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
player = Player()
all_sprites.add(player) 


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