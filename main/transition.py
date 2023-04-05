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
    FPS = 30

    with open('data/transitions.yml', 'r', encoding='utf8') as file:
        transitions = yaml.load(file, Loader=yaml.CLoader)

def check_events():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            os._exit(True)
            # pygame.quit()

global abc
abc=0
class Text():
    def __init__(self):#, text: str, amount_per_line: int):
       # self.text_list = [text[amount_per_line * i:amount_per_line * (i + 1)] for i in range(math.ceil(len(text) / amount_per_line))]
        print(1)
    def display(self, text: str, amount_per_line: int):
        global abc
        self.text_list = [text[amount_per_line * i:amount_per_line * (i + 1)] for i in range(math.ceil(len(text) / amount_per_line))]
        for i, text in enumerate(self.text_list):
            for j in range(len(text) + 1):
                clock.tick(FPS)
                #print(text[:j + 1])
                if(text_size* abc*2>= HEIGHT):
                    screen.fill('black')
                    abc=0
                text_surface = font.render(text[:j + 1], True, "white")
                text_rect = text_surface.get_rect(left=0, y=text_size* abc*2)
                # screen.fill('black')
                screen.blit(text_surface, text_rect) 
                pygame.display.update()
                check_events()
            abc+=1



init()

for transition in transitions:
    a = Text()
    a.display(transition, 25)