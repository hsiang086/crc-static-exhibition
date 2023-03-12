import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
FPS = 60
RES = W, H = (600,600)

center_x = W // 2
center_y = H // 2

pygame.init()

screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 40, bold=True)

#text displayer
def text_display(char, x, y, color):
    text = font.render(str(char), True, color)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((200,200))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, W - self.rect.width)
        self.rect.y = 0
        self.speedy = 5
    def update(self):
        self.rect.y += self.speedy

sprites = pygame.sprite.Group()
player = Player()
sprites.add(player)

running = True
while running:
    clock.tick(FPS)
    pygame.display.set_caption("main")
    screen.fill(BLACK)

    sprites.update()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
pygame.quit()