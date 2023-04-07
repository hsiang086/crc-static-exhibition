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

thanks_list.init()
second_scene.init()
third_scene.init()
while thanks_list.replay:
    init()
    transition.init()
    transition.display_conversation(transitions['first_scene'], 25)
    transition_transition()
    first_scene.init()
    first_scene.run()
    # transition_transition()

    transition.init()
    transition.display_conversation(transitions['second_scene'], 25)
    transition_transition()
    while second_scene.replay:
        second_scene.init()
        second_scene.run()
        if second_scene.replay == False:
            break
        transition.init()
        transition.display_conversation(transitions['second_second_scene'], 25)
        transition_transition()

    transition.init()
    transition.display_conversation(transitions['third_scene'], 25)
    transition_transition()
    while third_scene.replay:
        third_scene.init()
        third_scene.run()
        if third_scene.replay == False:
            break
        transition.init()
        transition.display_conversation(transitions['third_third_scene'], 25)
        transition_transition()

    transition.init()
    transition.display_conversation(transitions['last_scene'], 25)
    transition_transition()
    transition.init()
    transition.display_conversation(transitions['last_last_scene'], 25)
    transition_transition()
    thanks_list.last()