import colorsys
import pygame as pg

hue = 1
black = (0, 0, 0)
white = (255, 255, 255)
RES = W, H = 600, 600
FPS = 60

center_x = W//2
center_y = H//2
speed = 3
player = [center_x,center_y]

pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode(RES)
font = pg.font.SysFont("arial", 40, bold=True)

def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

def text_display(char, x, y):
    text = font.render(str(char), True, hsv2rgb(hue, 1, 1))
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)

one_x = 1
one_y = 0.5
running = True
while running:
    clock.tick(FPS)
    pg.display.set_caption("main")
    screen.fill(black)

    text_display("Hello world",player[0],player[1])
    if player[0] >= W or player[0] <= 0:
        one_x *= -1
        hue += 0.1
    if player[1] >= H or player[1] <= 0:
        one_y *= -1
        hue += 0.1

    player[0] += speed*one_x
    player[1] += speed*one_y

    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
pg.quit()