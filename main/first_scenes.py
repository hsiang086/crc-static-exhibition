import pygame
import os

def init():

    # global variable
    global WIDTH, HEIGHT, RES
    global screen

    global clock
    global FPS

    global first_scenes
    global lock_focusing
    global ascii_focusing

    # idk
    pygame.init()
    pygame.display.set_caption('CRC')

    # screen
    RES = WIDTH, HEIGHT = 768, 512
    screen = pygame.display.set_mode(RES)
    screen.fill('BLACK')

    # clock
    clock = pygame.time.Clock()
    FPS = 60

    # scenes
    first_scenes = pygame.sprite.Group()
    first_scenes.add(Door(), Lock(), Ascii())

    lock_focusing = pygame.sprite.Group()
    lock_focusing.add(DetailedLock(), Back(first_scenes))

    ascii_focusing = pygame.sprite.Group()
    ascii_focusing.add(DetailedAscii(), Back(first_scenes))



# back button
class Back(pygame.sprite.Sprite):
    def __init__(self, to_draw: pygame.sprite.Group):
        super().__init__()
        self.to_draw = to_draw
        self.image = pygame.image.load(os.path.join("images", "x.png")).convert()
        self.image = pygame.transform.scale(self.image, (40, 40))
        # self.image.set_colorkey("BLACK")
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH-10
        self.rect.top = 10

    def update(self):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(pygame.mouse.get_pos()):
                screen.fill('BLACK')
                self.to_draw.draw(screen)
    


# first scenes
class Door(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((200, 350))
        self.image.fill('WHITE')
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 15
        self.rect.y = HEIGHT // 10
    
class Lock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((WIDTH * 8 / 100, HEIGHT * 14 / 100))
        self.image.fill('BLUE')
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2.65
        self.rect.y = HEIGHT / 5

    def update(self):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(pygame.mouse.get_pos()):
                screen.fill('BLACK')
                lock_focusing.draw(screen)

class Ascii(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((WIDTH / 15, WIDTH / 15))
        self.image.fill('GREEN')
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH * 15 / 100
        self.rect.bottom = HEIGHT * 85 / 100

    def update(self):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(pygame.mouse.get_pos()):
                screen.fill('BLACK')
                ascii_focusing.draw(screen)

# lock focusing
class DetailedLock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((WIDTH * 48 / 100, HEIGHT * 84 / 100))
        self.image.fill('BLUE')
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2


# ascii focusing
class DetailedAscii(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join("images", "ascii list.png")).convert_alpha()
        # self.image = pygame.Surface((WIDTH * 2 / 5, WIDTH * 2 / 5))
        # self.image.fill('GREEN')
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2




init()
first_scenes.draw(screen)

while True:
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            os._exit(True)
        if event == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                os._exit(True)

    first_scenes.update()
    lock_focusing.update()
    pygame.display.update()