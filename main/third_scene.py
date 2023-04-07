import pygame
import os
import random
from math import sin, cos, pi, sqrt, pow, ceil, atan
import yaml
#import easteregg

def init():
    global FPS
    global RES, WIDTH, HEIGHT 
    global clock
    global screen
    global x_center, y_center

    global shooting
    global questions
    global question_scene
    global question_background
    global balloon
    global playerblood

    global shooting_scene
    global aim
    global bullet

    global text_size
    global font
    global balloon_decrease_bool
    global player_decrease_bool
    global bullet_bool

    global q
    global q_listinit
    global background_init
    global replay 


    RES = WIDTH, HEIGHT = 1920, 1080
    FPS = 60
    x_center, y_center = WIDTH / 2, HEIGHT / 2
    replay = True
    
    pygame.init()
    pygame.display.set_caption("third")
    screen = pygame.display.set_mode(RES, pygame.SCALED | pygame.FULLSCREEN | pygame.NOFRAME)
        
    bg_image = pygame.image.load("images/third_scene/bg.png").convert_alpha()
    def background_init():
        screen.blit(bg_image,(0,0))
    clock = pygame.time.Clock()
    text_size = 50
    font = pygame.font.Font('font/Cubic_11_1.013_R.ttf', text_size)

    shooting = False
    bullet_bool = False

    with open('data/questions.yml', 'r', encoding='utf8') as file:
        questions = yaml.load(file, Loader=yaml.CLoader)
    question_scene = pygame.sprite.Group()
    question_background = QuestionBackground()
    #player = Player()
    balloon = Balloon()
    balloon_decrease_bool = False
    player_decrease_bool = False
    balloonblood = BalloonBlood()
    balloonblooddecrease = BalloonBloodDecrease()
    playerblood = PlayerBlood()
    playerblooddecrease = PlayerBloodDecrease()
    #bullet_count = BulletCount()

    q = random.randrange(4)
    def q_listinit():
        global q_list
        q_list = [i for i in range(len(questions['questions']))]
    q_listinit()
    question_scene.add(balloon, question_background, balloonblood, balloonblooddecrease, playerblood, playerblooddecrease, [AnswerButton(i) for i in range(4)])

    shooting_scene = pygame.sprite.Group()
    aim = Aim()
    bullet = Bullet()
    shooting_scene.add(balloon, aim, balloonblood, balloonblooddecrease,bullet)
    shooting_scene.add(balloon, aim, bullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join("images/third_scene/ammo_icon.png")).convert_alpha()
        self.time = 0
        self.x = WIDTH
        self.y = HEIGHT + 30
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.speed = 20
        self.aim_bullet_length = pow(pow(aim.rect.centerx - self.rect.centerx, 2) + pow(aim.rect.centery - self.rect.centery, 2), 0.5)
        self.x_move = (abs(aim.rect.centerx - self.rect.centerx) / self.aim_bullet_length) * self.speed
        self.y_move = (abs(aim.rect.centery - self.rect.centery) / self.aim_bullet_length) * self.speed
        self.is_flying = False
        self.is_rotated = False
        self.angle = atan(abs(aim.rect.centery - self.rect.centery) / abs(aim.rect.centerx - self.rect.centerx))

    def update(self):
        global shooting
        if self.is_flying:
            if not self.is_rotated:
                self.image = pygame.transform.rotate(self.image, 45 - self.angle / pi * 180)
                print(self.angle)
                self.is_rotated = True
            self.rect.centerx -= self.x_move
            self.rect.centery -= self.y_move
            if balloon.rect.collidepoint(self.rect.center):
                self.rect.x = WIDTH
                self.time = 0
                self.rect.y = HEIGHT + 30
                self.is_flying = False
                balloon.change = not balloon.change
                balloon.size = 'small'
                global balloon_decrease_bool
                balloon_decrease_bool = True
                shooting = False
                aim.__init__()
                balloon.__init__()
            if self.rect.centery <= 0 or self.rect.centerx <= 0:
                self.image = pygame.image.load(os.path.join("images/third_scene/ammo_icon.png")).convert_alpha()
                self.is_rotated = False
                self.time += 1
                self.rect.x = WIDTH            
                self.rect.y = HEIGHT + 30
                self.is_flying = False
                if self.time >= 3:
                    self.time = 0
                    aim.__init__()
                    balloon.__init__()
                    shooting = False
        else:
            #m = abs(aim.rect.centery - self.rect.centery) / abs(aim.rect.centerx - self.rect.centerx)
            self.x_move = abs(aim.rect.centerx - self.rect.centerx) / self.aim_bullet_length * self.speed
            self.y_move = abs(aim.rect.centery - self.rect.centery) / self.aim_bullet_length * self.speed
            self.aim_bullet_length = pow(pow(aim.rect.centerx - self.rect.centerx, 2) + pow(aim.rect.centery - self.rect.centery, 2), 0.5)
            self.angle = atan(abs(aim.rect.centery - self.rect.centery) / abs(aim.rect.centerx - self.rect.centerx))
    # def reset(self):
    #     self.rect.centery = self.y

    # def update(self):
    #     global bullet_bool
    #     if bullet_bool:
    #         #print(self.rect.centery)
    #         if self.rect.centery <= 0:
    #             bullet_bool = False
    #             self.reset()
    #     else:
    #         self.rect.centerx = aim.rect.centerx
    #         self.reset()
    #         #print(self.rect.centerx)

class Aim(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join("images/third_scene/crosshair.png")).convert_alpha()
        #self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.speed = 5
        self.rect.centerx = x_center
        self.rect.centery = y_center
    def update(self):
        key = pygame.key.get_pressed()
        if (key[pygame.K_w] or key[pygame.K_UP]) and 0 <= self.rect.center[1]:
            self.rect.centery -= self.speed
        if (key[pygame.K_s] or key[pygame.K_DOWN]) and self.rect.center[1] <= HEIGHT:
            self.rect.centery += self.speed
        if (key[pygame.K_a] or key[pygame.K_LEFT]) and 0 <= self.rect.center[0]:
            self.rect.centerx -= self.speed
        if (key[pygame.K_d] or key[pygame.K_RIGHT]) and self.rect.center[0] <= WIDTH:
            self.rect.centerx += self.speed

class Balloon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join("images/third_scene/balloon_red.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (183.6, 243.9)) # the ratio is 204:271
        self.rect = self.image.get_rect()
        self.paused = False
        self.change = True
        self.size = 'small'
        self.theta = 0
        self.count = 0
        # circle radius
        self.movecircle_bool = True
        self.circle_speed = 3
        self.r = 150
        self.rect.centerx = x_center
        self.rect.centery = HEIGHT / 4.5
        self.circle_centerx = self.rect.centerx 
        self.circle_centery = self.rect.centery + self.r
        self.check = True
        self.bf_x = self.rect.centerx
        self.bf_y = self.rect.centery

        self.m_x = 1
        self.m_y = sqrt(3)
        self.triangle_speed = 3
        self.step = 45

        # 
        self.movetriangle_bool = not self.movecircle_bool

        self.bullet_is_flying = False

    def circlemotion(self):
        theta_degree = self.theta * 2 * pi / 360
        costheta, sintheta = cos(theta_degree), sin(theta_degree)
        # rotation matrix   https://en.wikipedia.org/wiki/Rotation_matrix
        self.rect.centerx = self.circle_centerx + self.r * sintheta
        self.rect.centery = self.circle_centery - self.r * costheta
        if self.theta == 360:
            self.check = True

    def trianglemotion(self):
        # m_x = 1
        # m_y = sqrt(3)
        # bf_bool = True
        

        self.bf_bool = True
        self.count += 1
        
        if self.count >= 3 * self.step:
            self.rect.centerx = int(self.bf_x) + 1
            self.rect.centery = int(self.bf_y) + 2
            self.count = 0
            self.bf_bool = False
            self.check = True

        if self.count < self.step:
            self.bf_x += self.m_x * self.triangle_speed
            self.bf_y += self.m_y * self.triangle_speed
        
        if self.count < 2 * self.step and self.count >= self.step:
            self.bf_x -= sqrt(pow(self.m_x, 2) + pow(self.m_y, 2)) * self.triangle_speed
            # self.rect.centery += m_y - m_y * speed
        
        if self.count < 3 * self.step and self.count >= 2 * self.step:
            self.bf_x += self.m_x * self.triangle_speed
            self.bf_y -= self.m_y * self.triangle_speed

        if self.bf_bool:
            self.rect.centerx = self.bf_x
            self.rect.centery = self.bf_y
            
     
    
    def update(self):
        #if rotation_bool:
        #    self.rotate_init()
        #    rotation_bool = False
        global balloon_decrease_bool
        global bullet_bool
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    self.check = True
                if event.key == pygame.K_SPACE and not bullet.is_flying: #and self.rect.collidepoint(bullet.rect.center):
                    #balloon_decrease_bool = True
                    bullet.is_flying = True

        if self.bullet_is_flying:
            if self.rect.collidepoint(bullet.rect.center):
                bullet.rect.x = WIDTH
                bullet.rect.y = HEIGHT + 30
                shooting_scene.remove(bullet)
                self.change = not self.change
                balloon_decrease_bool = True
                self.size = 'small'
                #     bullet_bool = True
                # if self.rect.collidepoint(bullet.rect.center):
                #     print("balloon",self.rect.center)
                #     print("bullet",bullet.rect.center)
                #     print("hellllllllllppppppppp!!!!!!!")
                #     bullet_bool = False
                #     self.change = not self.change
                #     balloon_decrease_bool = True
                #     global shooting
                #     shooting = not shooting
        if self.size == 'large' and self.theta == 0 and self.count == 0:
            self.r = 350
            self.circle_speed = 1
            self.step = 120
        if self.size == 'small' and self.theta == 0 and self.count == 0:
            self.r = 150
            self.step = 45


        
        if self.check:
            rand_num = random.randint(0,1)
            if rand_num == 0:
                self.movecircle_bool = True
                self.circle_centerx = self.rect.centerx 
                self.circle_centery = self.rect.centery + self.r
            else :
                self.movecircle_bool = False
            if rand_num == 1:
                self.movetriangle_bool = True
                self.bf_x = self.rect.centerx
                self.bf_y = self.rect.centery
            else :
                self.movetriangle_bool = False
            self.check = False
        if not self.paused:
            if self.movecircle_bool:
                self.theta += self.circle_speed
                self.circlemotion()
            if self.movetriangle_bool:
                self.trianglemotion()
            self.theta %= 360

class BalloonBlood(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((150,25))
        self.image.fill('white')
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH - 20
        self.rect.top = 20
    
class BalloonBloodDecrease(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 140
        self.image = pygame.Surface((self.width,15))
        self.image.fill('red')
        self.decrease = False
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH - 165
        self.rect.top = 25
        self.count = 0
        self.step = 60
        self.bloodstep = True
        self.bf = 0

    def update(self):
        global balloon_decrease_bool
        self.decrease = balloon_decrease_bool
        if self.decrease and self.count < self.step:
            self.width -= 30 / self.step
            self.count +=  1
            if self.bf % 5 == 0:
                self.bloodstep = not self.bloodstep
            if self.bloodstep:
                self.bf += 1
                if self.width == 0:
                    global running
                    global replay
                    replay = False
                    running = False
                self.image = pygame.Surface((self.width,15))
                self.image.fill('red')
            else:
                self.image = pygame.Surface((self.width,15))
                self.image.fill('grey')
        elif self.decrease and self.count == self.step:
            self.count = 0
            balloon_decrease_bool = False

class PlayerBlood(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((150,25))
        self.image.fill('white')
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH - 20
        self.rect.top = HEIGHT - 50

class PlayerBloodDecrease(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 140
        self.image = pygame.Surface((self.width,15))
        self.image.fill('red')
        self.decrease = False
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH - 165
        self.rect.top = HEIGHT - 45
        self.count = 0
        self.step = 60
        self.bloodstep = True
        self.bf = 0

    def update(self):
        global player_decrease_bool
        self.decrease = player_decrease_bool
        if self.decrease and self.count < self.step:
            self.width -= 30 / self.step
            self.count +=  1
            if self.bf % 5 == 0:
                self.bloodstep = not self.bloodstep
            if self.bloodstep:
                self.bf += 1
                if self.width == 0:
                    global running
                    running = False
                self.image = pygame.Surface((self.width,15))
                self.image.fill('red')
            else:
                self.image = pygame.Surface((self.width,15))
                self.image.fill('grey')
        elif self.decrease and self.count == self.step:
            self.count = 0
            player_decrease_bool = False
       
class QuestionBackground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/third_scene/frame/main_frame.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH * 1 / 2
        self.rect.centery = HEIGHT * 7 / 9
        # self.rect.left = WIDTH * 6 / 100
        # self.rect.centery = y_center + HEIGHT * 5 / 18
    
class AnswerButton(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        # self.image = pygame.Surface((question_background.image.get_width() / 7.5, question_background.image.get_height() / 5))
        # self.image.fill("yellow")
        self.num = pos
        self.image = pygame.image.load(f'images/third_scene/frame/button_{self.num}.png')
        self.rect = self.image.get_rect()
        self.pos = pos - 2
        self.rect.left = 10 + question_background.rect.centerx + self.pos * ((question_background.rect.right - question_background.rect.left) / 4)
        self.rect.centery = question_background.rect.bottom - 80

    def switch_q(self):
        global q
        if len(q_list) == 1:
            q_listinit()
        q_list.remove(q)
        q = random.choice(q_list)

    def update(self):
        global q_list, shooting, balloon, player_decrease_bool
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(pygame.mouse.get_pos()) and not player_decrease_bool:
                if questions['answer'][q] == self.num:
                    shooting = True
                    balloon.size = 'large'
                    self.switch_q()
                else:
                    player_decrease_bool = True
                    self.switch_q()

class Question():
    def __init__(self, question_index: int, amount_per_line: int):
        question = questions['questions'][question_index]
        self.text_list = [question[amount_per_line * i:amount_per_line * (i + 1)] for i in range(ceil(len(question) / amount_per_line))]

    def display(self):
        for i, char in enumerate(self.text_list):
            text = font.render(str(char), True, "white")
            text_rect = text.get_rect(topleft=(question_background.rect.left * 1.6, question_background.rect.top * 1.1 + (text_size * i)))
            screen.blit(text, text_rect)

# class BulletCount(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.Surface((50,100))
#         self.image.fill((1,146,46))
#         self.rect = self.image.get_rect()
#         self.rect.centerx = WIDTH - 50
#         self.rect.centery = HEIGHT - 50


init()
def run():
    global running
    running = True
    while running:
        global events
        clock.tick(FPS)
        events = pygame.event.get()

        background_init()
        
        if not shooting:
            question_scene.draw(screen)
            ques = Question(q, 30)
            ques.display()
            question_scene.update()
        else:
            background_init()
            shooting_scene.draw(screen)
            shooting_scene.update()

        pygame.display.update()