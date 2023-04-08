import pygame
import random
def run():
    pygame.init()

    RES = SW, SH = (1920,1080)

    BLOCK_SIZE = 60
    FONT = pygame.font.Font("font\\Cubic_11_1.013_R.ttf", BLOCK_SIZE*2)

    screen = pygame.display.set_mode(RES, pygame.SCALED | pygame.FULLSCREEN | pygame.NOFRAME)
    pygame.display.set_caption("Snake!")
    pygame.display.set_icon(pygame.image.load('images/icon.png'))
    clock = pygame.time.Clock()
    global paused
    paused = False
    global speed
    speed = 5
    class Snake:
        def __init__(self):
            self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
            self.xdir = 1
            self.ydir = 0
            self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
            self.body = [pygame.Rect(self.x-BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
            self.dead = False
        
        def update(self):
            global apple
            
            for square in self.body:
                if self.head.x == square.x and self.head.y == square.y:
                    self.dead = True
                if self.head.x not in range(0, SW) or self.head.y not in range(0, SH):
                    self.dead = True
            
            if self.dead:
                self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
                self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
                self.body = [pygame.Rect(self.x-BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
                self.xdir = 1
                self.ydir = 0
                self.dead = False
                global paused
                paused = True
                global speed
                speed = 5
                apple = Apple()
            
            self.body.append(self.head)
            for i in range(len(self.body)-1):
                self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
            self.head.x += self.xdir * BLOCK_SIZE
            self.head.y += self.ydir * BLOCK_SIZE
            self.body.remove(self.head)

    class Apple:
        def __init__(self):
            self.x = int(random.randint(0, SW)/BLOCK_SIZE) * BLOCK_SIZE
            self.y = int(random.randint(0, SH)/BLOCK_SIZE) * BLOCK_SIZE
            self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        
        def update(self):
            pygame.draw.rect(screen, "red", self.rect)

    def drawGrid():
        for x in range(0, SW, BLOCK_SIZE):
            for y in range(0, SH, BLOCK_SIZE):
                rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(screen, "#3c3c3b", rect, 1)

    score = FONT.render("1", True, "white")
    score_rect = score.get_rect(center=(SW/2, SH/20))

    drawGrid()

    snake = Snake()

    apple = Apple()

    running = True

    

    n = 0
    
    while running:
        n += 1
        if n % (speed * speed) == 0:
            speed += 1
        
        while paused:
            score1 = FONT.render("YOU DIED, ENTER TO RETRY,", True, "white")
            score2 = FONT.render(" ESC TO QUIT", True, "white")
            screen.fill('black')
            screen.blit(score1, (0, 0))
            screen.blit(score2, (0, 100))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        paused = False
                    elif event.key == pygame.K_ESCAPE:
                        paused = False
                        running = False
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    snake.ydir = 1
                    snake.xdir = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    snake.ydir = -1
                    snake.xdir = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    snake.ydir = 0
                    snake.xdir = 1
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    snake.ydir = 0
                    snake.xdir = -1

        snake.update()
        
        screen.fill('black')
        drawGrid()

        apple.update()

        score = FONT.render(f"{len(snake.body) + 1}", True, "white")

        pygame.draw.rect(screen, "green", snake.head)

        for square in snake.body:
            pygame.draw.rect(screen, "green", square)

        screen.blit(score, score_rect)

        if snake.head.x == apple.x and snake.head.y == apple.y:
            snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
            apple = Apple()

        pygame.display.update()
        clock.tick(speed)
