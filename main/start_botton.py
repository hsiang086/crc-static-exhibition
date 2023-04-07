import pygame
def init():
    global WIDTH, HEIGHT, RES
    global screen
    global FPS
    global running
    global clock
    global scene

    RES = WIDTH, HEIGHT = 1920,1080
    FPS = 60
    running = True
    
    pygame.init()
    pygame.display.set_caption("last")
    screen = pygame.display.set_mode(RES)
    clock = pygame.time.Clock()
    scene = pygame.sprite.Group()
    start_button = StartButton()
    scene.add(start_button)

class StartButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.image = pygame.image.load("images/transparent.png").convert_alpha()
        # self.image = pygame.transform.scale(self.image,(420,200))
        self.image = pygame.Surface((420,200))
        self.image.fill("white")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2 + 10, HEIGHT - 315)

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
