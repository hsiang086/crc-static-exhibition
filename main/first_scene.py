import pygame
import os

def init():

    # global variable
    global WIDTH, HEIGHT, RES
    global screen

    global font
    global clock
    global FPS

    global typing, end_type

    global desktop
    global lock_focusing
    global ascii_scene
    
    global IPBw,IPBh,IPBx,IPBy
    global answer, correct
    
    typing = False
    end_type = False
    correct = False
    answer = "hsnucrc"
    # idk
    pygame.init()
    pygame.display.set_caption('first scene')

    #font
    font = pygame.font.SysFont('Arial', 20, bold=True)

    # screen
    RES = WIDTH, HEIGHT = 1920, 1080
    IPBw = 140
    IPBh = 32
    IPBx = (WIDTH / 2) - IPBw
    IPBy = (HEIGHT / 2) - IPBh
    screen = pygame.display.set_mode(RES)
    screen.fill('BLACK')


    # clock
    clock = pygame.time.Clock()
    FPS = 60

    # scenes
    desktop = pygame.sprite.Group()
    desktop.add(Wallpaper(), Lock(), AsciiButton())

    lock_focusing = pygame.sprite.Group()
    lock_focusing.add(Back(desktop, (1800, 45)))

    ascii_scene = pygame.sprite.Group()
    ascii_scene.add(AsciiFile(), Back(desktop, pos=(1800, 45)))



# back button
class Back(pygame.sprite.Sprite):
    def __init__(self, to_draw: pygame.sprite.Group, pos: tuple):
        super().__init__()
        self.to_draw = to_draw
        self.image = pygame.image.load(os.path.join("images", "x.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(pygame.mouse.get_pos()):
                screen.fill('BLACK')
                self.to_draw.draw(screen)
                inputbox.disappear()
    
class InputBox():
    def __init__(self, rect: pygame.Rect):
        self.boxBody: pygame.Rect = rect
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.active = False
        self.text = ''
        self.done = False
        self.font = pygame.font.Font(None, 32)
        self.width = 200

    def dealEvent(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.boxBody.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
        
    def draw(self, screen: pygame.surface.Surface):
        txtSurface = self.font.render(self.text, True, self.color)
        self.width = max(200, txtSurface.get_width()+10)
        self.boxBody.w = self.width
        screen.blit(txtSurface, (self.boxBody.x+5, self.boxBody.y+5))
        pygame.draw.rect(screen, self.color, self.boxBody, 2)

    def disappear(self):  
        global typing 
        typing = False 

    def update(self):
        self.color = self.color_active if self.active else self.color_inactive

def Type_PW():
    global inputbox
    global IPBw,IPBh,IPBx,IPBy
    inputbox = InputBox(pygame.Rect(IPBx, IPBy, IPBw, IPBh))
   

class Confirm(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100,IPBh))    
        self.image.fill((153,153,0))
        self.rect = self.image.get_rect()
        self.rect.y = IPBy

    def dealEvent(self,inputbox: InputBox):
        global correct
        self.image.fill((255,255,255))
        if inputbox.text == answer:
            correct = True
        else:
            correct = False
            inputbox.text = ""   
        print(correct)            

    def disappear(self):
        self.kill()

    def update(self,inputbox:InputBox):
        self.rect.x = IPBx + inputbox.width + 10  


# first scenes
class Wallpaper(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/first_scene/desktop.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
    

class AsciiFile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/first_scene/ascii.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
    
class Lock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/first_scene/icon/lock.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (134, 171))
        self.image.set_colorkey("BLACK")
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2.65
        self.rect.y = HEIGHT / 5

    def update(self):
        global typing
        global confirm, confirm_bottons
        for event in events:
            confirm = Confirm()
            confirm_bottons = pygame.sprite.Group()
            confirm_bottons.add(confirm)
            if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(pygame.mouse.get_pos()) and not inputbox.active:
                screen.fill('BLACK')
                typing = True        
            inputbox.dealEvent(event) 
            
             
            if typing:
                screen.fill('BLACK')
                lock_focusing.update()
                inputbox.draw(screen)      
        if typing: 
            lock_focusing.draw(screen)
            confirm.update(inputbox)     
            confirm_bottons.draw(screen)   
               


class AsciiButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/first_scene/icon/prtsc.png").convert_alpha()
        # # self.image = pygame.transform.scale(self.image, (134, 171))
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH * 15 / 100
        self.rect.bottom = HEIGHT * 85 / 100

    def update(self):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(pygame.mouse.get_pos()):
                ascii_scene.draw(screen)


init()
desktop.draw(screen)
Type_PW()

while True:
    clock.tick(FPS)
    events = pygame.event.get()


    for event in events:
        if event.type == pygame.QUIT:
            os._exit(True)
        if event == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                os._exit(True)
        if typing:
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if confirm.rect.collidepoint(pygame.mouse.get_pos()):
                    confirm.dealEvent(inputbox)
                    print(correct)
 

    desktop.update()
    lock_focusing.update()
                    
    if correct:
        os._exit(True)    
                      
    pygame.display.update()