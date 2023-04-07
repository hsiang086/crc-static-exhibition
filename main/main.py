import pygame
import os
import yaml
import transition
import first_scene
import second_scene
import third_scene
import thanks_list
import start_botton

def init():
    global running
    global transitions
    running = True
    with open('data/transitions.yml', 'r', encoding='utf8') as file:
        transitions = yaml.load(file, Loader=yaml.CLoader)


thanks_list.init()
second_scene.init()
third_scene.init()
while thanks_list.replay:
    init()
    start_botton.init()
    start_botton.run()
    transition.init()
    transition.display_conversation(transitions['first_scene'], 25)
    first_scene.init()
    first_scene.run()

    transition.init()
    transition.display_conversation(transitions['second_scene'], 25)
    while second_scene.replay:
        second_scene.init()
        second_scene.run()
        if second_scene.replay == False:
            break
        transition.init()
        transition.display_conversation(transitions['second_second_scene'], 25)

    transition.init()
    transition.display_conversation(transitions['third_scene'], 25)
    while third_scene.replay:
        third_scene.init()
        third_scene.run()
        if third_scene.replay == False:
            break
        transition.init()
        transition.display_conversation(transitions['third_third_scene'], 25)

    transition.init()
    transition.display_conversation(transitions['last_scene'], 25)
    transition.init()
    transition.display_conversation(transitions['last_last_scene'], 25)
    thanks_list.last()