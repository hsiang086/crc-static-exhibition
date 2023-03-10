import os
import pygame as pg

surface = pg.display.get_surface()
white = (255, 255, 255)
RES = W, H = 0,0
FPS = 60

pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)

running = True
while running:
    clock.tick(FPS)
    pg.display.set_caption("main")
    screen.fill(white)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
pg.quit()