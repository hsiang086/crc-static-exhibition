import pygame
import os
import yaml
import transition
import first_scene
import second_scene
import third_scene
import thanks_list

def init():
    global running
    global transitions
    running = True
    with open('data/transitions.yml', 'r', encoding='utf8') as file:
        transitions = yaml.load(file, Loader=yaml.CLoader)

def check_events():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.MOUSEBUTTONUP or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (event.type == pygame.KEYUP and event.key == pygame.K_RETURN):
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
thanks_list.init()
transition.init()

while thanks_list.replay:
    transition.display_conversation(transitions['first_scene'], 25)
    transition_transition()
    first_scene.init()
    first_scene.run()
    # transition_transition()

    transition.display_conversation(transitions['second_scene'], 25)
    transition_transition()
    second_scene.init()
    second_scene.run()

    transition.display_conversation(transitions['third_scene'], 25)
    transition_transition()
    third_scene.init()
    third_scene.run()

    transition.display_conversation(transitions['last_scene'], 25)
    transition_transition()
    thanks_list.last()