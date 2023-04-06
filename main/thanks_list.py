import pygame

def init():
    global FPS
    global RES, WIDTH, HEIGHT 
    global clock
    global screen
    global running
    global scene
    global last_thanks
    global quit_button
    global replay_button
    global easter_egg_button
    global replay
    
    RES = WIDTH, HEIGHT = 1920, 1080
    FPS = 120
    running = True
    replay = True
    
    pygame.init()
    pygame.display.set_caption("last")
    screen = pygame.display.set_mode(RES)
    clock = pygame.time.Clock()

    scene = pygame.sprite.Group()
    last_thanks = LastThanks()
    quit_button = QuitButton()
    replay_button = ReplayButton()
    easter_egg_button = EasterEggButton()
    scene.add(last_thanks)

class LastThanks(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 3
        self.check_button = True
        self.image = pygame.image.load("images/last thanks.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.top = HEIGHT

    def update(self):
        if self.rect.bottom > HEIGHT :
            self.rect.bottom -= self.speed
        elif self.check_button :
            scene.add(quit_button,replay_button,easter_egg_button)
            self.check_button = False

class EasterEggButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/transparent.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(420,200))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2 + 10, HEIGHT - 920)

    def update(self):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(pygame.mouse.get_pos()):
                pygame.quit()

class ReplayButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/transparent.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(420,200))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2 + 10, HEIGHT - 580)

    def update(self):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(pygame.mouse.get_pos()):
                global replay
                global running
                replay = True
                running = False

class QuitButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/transparent.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(420,200))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2 + 10, HEIGHT - 315)

    def update(self):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(pygame.mouse.get_pos()):
                global running
                global replay
                running = False
                replay = False

def last():

    init()

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