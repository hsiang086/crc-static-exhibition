import pygame
def init():
    global WIDTH, HEIGHT, RES
    global screen
    global FPS
    global running
    global clock
    global scene
    global speed
    global i,ialpha
    global luck_y

    RES = WIDTH, HEIGHT = 1920,1080
    FPS = 60
    running = True
    speed = 5
    i = -1
    ialpha = 1
    luck_y = 200
    
    pygame.init()
    pygame.display.set_caption("last")
    screen = pygame.display.set_mode(RES, pygame.SCALED | pygame.FULLSCREEN | pygame.NOFRAME)
    clock = pygame.time.Clock()
    scene = pygame.sprite.Group()
    start_button = StartButton()
    luckymove = LuckyMove()
    luckymovealpha = LuckyMoveAlpha()
    luckymoveamain = LuckyMoveMain()
    bg = BackGround()
    scene.add(bg,start_button,luckymove,luckymovealpha,luckymoveamain)

class BackGround(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/start bg.png").convert_alpha()
        # self.image = pygame.Surface((200,200))
        # self.image.fill("white")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2,HEIGHT / 2)

class LuckyMove(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/second_scene/障礙物1 去背.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(400,400))
        # self.image = pygame.Surface((200,200))
        # self.image.fill("white")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2,luck_y)

    def update(self):
        global i
        if self.rect.centerx <= WIDTH / 2:
            i *= -1
        elif self.rect.right >= WIDTH :
            i *= -1
        self.rect.centerx += speed * i

class LuckyMoveAlpha(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/second_scene/障礙物2 去背.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(400,400))
        # self.image = pygame.Surface((200,200))
        # self.image.fill("white")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2,luck_y)

    def update(self):
        global ialpha
        if self.rect.centerx >= WIDTH / 2:
            ialpha *= -1
        elif self.rect.right <= 0 :
            ialpha *= -1
        self.rect.centerx -= speed * i

class LuckyMoveMain(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/second_scene/障礙物3 去背.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(500,500))
        # self.image = pygame.Surface((200,200))
        # self.image.fill("white")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2,luck_y)
       

class StartButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((420, 200)).convert_alpha()
        self.image.fill((0, 0, 0, 0))
        # self.image = pygame.Surface((420,200))
        # self.image.fill("white")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 315)

    def update(self):
        for event in events:
            if (event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(pygame.mouse.get_pos())) or (event.type == pygame.KEYUP and event.key == pygame.K_RETURN):
                global running
                running = False
init()
def run():
    global running
    while running:
        global events
        clock.tick(FPS)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        scene.update()
        scene.draw(screen)
        pygame.display.update()