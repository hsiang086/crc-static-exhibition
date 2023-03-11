import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
RES = W, H = (600,600)

center_x = W // 2
center_y = H // 2

#road quantity
r_q = 3
pixel_w = W // r_q

pygame.init()

player = pygame.Surface((pixel_w,pixel_w))
player.fill(WHITE)
player_x = 0

screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 40, bold=True)

def text_display(char, x, y, color):
    text = font.render(str(char), True, color)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)
right, left = 0, 0
running = True
while running:
    clock.tick(FPS)
    pygame.display.set_caption("main")
    screen.fill(BLACK)
    player_x += ((right+left) * pixel_w)
    right, left = 0, 0
    if player_x > W - pixel_w:
        player_x = W - pixel_w
    elif player_x < 0:
        player_x = 0
    screen.blit(player,(player_x,H-pixel_w))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                right = 1
            if event.key == pygame.K_LEFT or  event.key == pygame.K_a:
                left = -1
pygame.quit()