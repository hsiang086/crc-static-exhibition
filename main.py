import os
import pygame as pg

white = (255, 255, 255)
RES = W, H = 600, 600
FPS = 60

pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode(RES)

running = True
while running:
    clock.tick(FPS)
    pg.display.set_caption("pygame")
    screen.fill(white)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
pg.quit()