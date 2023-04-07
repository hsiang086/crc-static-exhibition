import pygame
import yaml

def init():    
    global WIDTH, HEIGHT, RES
    global screen
    global FPS
    global running
    global clock
    global font
    global frame_list
    global font_size


    RES = WIDTH, HEIGHT = 1920, 1080
    FPS = 30
    running = True

    print('loading')
    with open('data/bad_apple.yml', 'r') as file:
        frame_list = yaml.load(file, Loader=yaml.CLoader)
    print('cpmpelete')

    
    pygame.init()
    pygame.display.set_caption("Bad Apple!!")
    screen = pygame.display.set_mode(RES, pygame.SCALED | pygame.FULLSCREEN | pygame.NOFRAME)
    clock = pygame.time.Clock()
    font_size = 22
    font = pygame.font.SysFont('MS Gothic', font_size, bold=False, italic=False)

def run():
    global running, font_size
    frame = 0
    while running:
        clock.tick(30)
        screen.fill('black')
        if not frame >= len(frame_list):
            ascii_list = frame_list[frame].split('\n')
            for i, ascii in enumerate(ascii_list):
                screen.blit(font.render(ascii, False, 'white'), (0, font_size * i))
                ii = i
            screen.blit(font.render('ESC to QUIT!', False, 'white'), (0, font_size * (ii + 2)))
            pygame.display.update()
            frame += 1
        else:
            running = False

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

if __name__ == '__main__':
    init()
    run()