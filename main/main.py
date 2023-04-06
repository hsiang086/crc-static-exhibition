import pygame
import os
from transition import transitionfunc
import first_scene
import second_scene
import third_scene

def init():
    global running
    running = True

def check_events():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.MOUSEBUTTONUP or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            global running 
            running= False
        if event.type == pygame.QUIT:
            os._exit(True)

def transition_transition():
    global running
    while running:
        check_events()
    running = True

init()

transitionfunc("data/transitions_first.yml")
transition_transition()
first_scene.init()
first_scene.run()
transition_transition()
transitionfunc("data/transitions_second.yml")
transition_transition()
second_scene.init()
second_scene.run()
transitionfunc("data/transitions_third.yml")
transition_transition()
third_scene.init()
third_scene.run()
transitionfunc("data/transitions_last.yml")
transition_transition()