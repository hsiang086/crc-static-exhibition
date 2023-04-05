import pygame
import os
import yaml
import math

def init():

    # global variable
    global WIDTH, HEIGHT, RES
    global screen

    global font
    global text_size

    global clock
    global FPS

    global transitions
    global continue_
    global continue_group

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


    continue_=Continue()
    continue_group = pygame.sprite.Group()
    continue_group.add(continue_)

def check_events():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            os._exit(True)
            # pygame.quit()

global abc
abc=0
class Text():
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
                screen.blit(text_surface, text_rect) 
                #screen.fill('black')
                continue_group.draw(screen)
                continue_group.update()
                pygame.display.update()
                check_events()
            abc+=1

class Continue(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/continue button.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH-50, HEIGHT - 50)
        self.change = True
        self.count = 1
        # flashing speed
        self.step = 3
    
    def update(self):
        self.count %= self.step
        if self.count == 1:
            if self.change:
                self.image = pygame.image.load("images/continue button.png").convert_alpha()
                self.image = pygame.transform.scale(self.image,(50,50))
                self.change = not self.change
            else:
                self.image = pygame.Surface((50,50))
                self.change = not self.change
        self.count += 1

# class ContinueBack(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.Surface(50,50)
#         self.rect = self.image.get_rect()
#         self.rect.center = continue_.rect.center

#     def update(self):
#         if continue_.change:
#             self.image = pygame.Surface(50,50)




init()

for transition in transitions:
    a = Text()
    a.display(transition, 25)