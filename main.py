import os
import pygame as pg

black = (0, 0, 0)
white = (255, 255, 255)
RES = W, H = 600, 600
FPS = 60

center_x = W//2
center_y = H//2
speed = 5
player = [center_x,center_y]

pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode(RES)
font = pg.font.SysFont("arial", 20, bold=True)

def text_display(char, x, y):
    text = font.render(str(char), True, black)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)

running = True
while running:
    clock.tick(FPS)
    pg.display.set_caption("main")
    screen.fill(white)

    text_display("Hello world",player[0],player[1])


    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
pg.quit()