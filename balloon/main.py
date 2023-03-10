import pygame

FPS = 60
RES = W, H = (600,600)

center_x = W // 2
center_y = H // 2

pygame.init()
screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 40, bold=True)
def text_display(char, x, y):
    text = font.render(str(char), True, (255,255,255))
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)

running = True

while running:
    clock.tick(FPS)
    pygame.display.set_caption("main")
    screen.fill((0,0,0))
    text_display("Hello world",center_x,center_y)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            paused = not paused
pygame.quit()