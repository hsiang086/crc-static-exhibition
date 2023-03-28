import pygame

def init():
    global FPS
    global RES, WIDTH, HIGHT
    global clock
    FPS = 60
    RES = WIDTH, HIGHT = (700, 900)
    clock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption("second scene")

init()
running = True
while running:
    clock.tick(FPS)
    pygame.display.update()
    events = pygame.event()
pygame.quit()