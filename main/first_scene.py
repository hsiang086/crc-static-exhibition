import pygame
import os

def init():

    # global variable
    global WIDTH, HEIGHT, RES
    global screen

    global font
    global clock
    global FPS

    global typing
    global first_scenes
    global lock_focusing
    global ascii_focusing

    typing = False

    # idk
    pygame.init()
    pygame.display.set_caption('first scene')

    #font
    font = pygame.font.SysFont('Arial', 20, bold=True)

    # screen
    RES = WIDTH, HEIGHT = 752, 480
    screen = pygame.display.set_mode(RES)
    screen.fill('BLACK')

    # clock
    clock = pygame.time.Clock()
    FPS = 60

    # scenes
    first_scenes = pygame.sprite.Group()
    first_scenes.add(PcScreen(), Lock(), Ascii())

    lock_focusing = pygame.sprite.Group()
    lock_focusing.add(Back(first_scenes))

    ascii_focusing = pygame.sprite.Group()
    ascii_focusing.add(DetailedAscii(), Back(first_scenes))



# back button
class Back(pygame.sprite.Sprite):
    def __init__(self, to_draw: pygame.sprite.Group):
        super().__init__()
        self.to_draw = to_draw
        self.image = pygame.image.load(os.path.join("images", "x.png")).convert()
        self.image = pygame.transform.scale(self.image, (40, 40))
        # self.image.set_colorkey("BLACK")
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH-10
        self.rect.top = 10

    def update(self):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(pygame.mouse.get_pos()):
                screen.fill('BLACK')
                self.to_draw.draw(screen)
                inputbox.disappear()
    
class InputBox:
    def __init__(self, rect: pygame.Rect):
        self.boxBody: pygame.Rect = rect
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.active = False
        self.text = ''
        self.done = False
        self.font = pygame.font.Font(None, 32)

    def dealEvent(self, event: pygame.event.Event):
        if(event.type == pygame.MOUSEBUTTONDOWN):
            if(self.boxBody.collidepoint(event.pos)):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if(
                self.active) else self.color_inactive
        if(event.type == pygame.KEYDOWN):
            if(self.active):
                if(event.key == pygame.K_RETURN):
                    print(self.text)
                elif(event.key == pygame.K_BACKSPACE):
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self, screen: pygame.surface.Surface):
        txtSurface = self.font.render(self.text, True, self.color)
        width = max(200, txtSurface.get_width()+10)
        self.boxBody.w = width
        screen.blit(txtSurface, (self.boxBody.x+5, self.boxBody.y+5))
        pygame.draw.rect(screen, self.color, self.boxBody, 2)
    def disappear(self):  
        global typing 
        typing = False 

def Type_PW():
    global inputbox
    inputbox = InputBox(pygame.Rect(WIDTH/2-70, HEIGHT/2+16, 140, 32))
    

# first scenes
class PcScreen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(RES)
        self.image.fill('WHITE')
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
    
class Lock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((WIDTH * 8 / 100, HEIGHT * 14 / 100))
        self.image.fill('BLUE')
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2.65
        self.rect.y = HEIGHT / 5

    def update(self):
        global typing
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(pygame.mouse.get_pos()) and not inputbox.active:
                if not inputbox.active:screen.fill('BLACK')
                lock_focusing.draw(screen)
                typing = True
                
            inputbox.dealEvent(event) 
            if typing:
                if inputbox.active: screen.fill('BLACK')
                lock_focusing.update()
                inputbox.draw(screen)
               


class Ascii(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((WIDTH / 15, WIDTH / 15))
        self.image.fill('GREEN')
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH * 15 / 100
        self.rect.bottom = HEIGHT * 85 / 100

    def update(self):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(pygame.mouse.get_pos()):
                screen.fill('BLACK')
                ascii_focusing.draw(screen)






# ascii focusing
class DetailedAscii(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join("images", "ascii list.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2




init()
first_scenes.draw(screen)
Type_PW()

while True:
    clock.tick(FPS)
    events = pygame.event.get()
    first_scenes.update()
    lock_focusing.update()
    for event in events:
        if event.type == pygame.QUIT:
            os._exit(True)
        if event == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                os._exit(True)
        
                      
    pygame.display.update()