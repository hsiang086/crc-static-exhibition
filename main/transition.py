import pygame
import os
import yaml
import math
import time

def init():

    # global variable
    global WIDTH, HEIGHT, RES
    global screen

    global font
    global text_size

    global clock
    global FPS

    global transitions


    # idk
    pygame.init()
    pygame.display.set_caption('first scene')

    #font
    text_size = 45
    font = pygame.font.Font('font/Cubic_11_1.013_R.ttf', text_size)
    # screen
    RES = WIDTH, HEIGHT = 1280, 720
    screen = pygame.display.set_mode(RES)
    screen.fill('BLACK')

    # clock
    clock = pygame.time.Clock()
    FPS = 8

    with open('data/transitions.yml', 'r', encoding='utf8') as file:
        transitions = yaml.load(file, Loader=yaml.CLoader)

def check_events():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            os._exit(True)
            # pygame.quit()


class Text():
    def __init__(self, text: str, amount_per_line: int):
        self.text_list = [text[amount_per_line * i:amount_per_line * (i + 1)] for i in range(math.ceil(len(text) / amount_per_line))]

    def display(self):
        for i, text in enumerate(self.text_list):
            for j in range(len(text) + 1):
                clock.tick(FPS)
                print(text[:j + 1])
                text_surface = font.render(text[:j + 1], True, "white")
                text_rect = text_surface.get_rect(left=0, y=text_size * i)
                screen.fill('black')
                screen.blit(text_surface, text_rect) 
                pygame.display.update()
                check_events()



init()

for transition in transitions:
    a = Text(transition, 25)
    a.display()