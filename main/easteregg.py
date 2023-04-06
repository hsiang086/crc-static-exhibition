import pygame
from pyvideoplayer import Video

def init():
    global FPS
    global RES, WIDTH, HIGHT
    global clock, screen

    FPS = 120
    RES = WIDTH, HIGHT = (1920, 1080)
    
    pygame.init()
    pygame.display.set_caption("transition")
    screen = pygame.display.set_mode(RES)
    clock = pygame.time.Clock()



def intro():
    opening_video = Video("images\RAnggyu.mp4")
    opening_video.set_size(RES)
    while True:
        opening_video.draw(screen, (0, 0), force_draw=False)
        pygame.display.update()
        clock.tick(FPS)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                

init()
intro()
# running = True
# while running:
#     clock.tick(FPS)
#     events = pygame.event.get()
#     for event in events:
#         if event.type == pygame.QUIT:
#             pygame.quit()
#     pygame.display.update()