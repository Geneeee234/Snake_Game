#SNAKE GAME
import pygame
import sys
import random

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
my_font = pygame.font.SysFont("monospace", 30)

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
SILVER = (192, 192, 192)

HEIGHT = 630
WIDTH = 600

BOX_SIZE = 30

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SNAKES!")

class box:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

direction = [False, False, True, False]

def draw_grid(w, h, c):
    for hor in range(0, 630, 30):
        pygame.draw.line(window, c, (0, hor), (w, hor))
    for ver in range(0, 600, 30):
        pygame.draw.line(window, c, (ver, 30), (ver, h))

def move(snake, dir):
    pos = [snake.x, snake.y]
    if dir[0] == True:
        pos[0] -= 30
        if pos[0] < 0:
            pos[0] = 570
        return pos
    elif dir[1] == True:
        pos[1] -= 30
        if pos[1] < 30:
            pos[1] = 600
        return pos
    elif dir[2] == True:
        pos[0] += 30
        if pos[0] > 570:
            pos[0] = 0
        return pos
    else:
        pos[1] += 30
        if pos[1] > 600:
            pos[1] = 30
        return pos
def eat(snake, food, speed, score, tails, BLUE):
    if snake.x == food.x and snake.y == food.y:
        speed += 1
        score += 1
        tails.append(box(BLUE, food.x, food.y))
        food.x = random.randint(1, 19) * 30
        food.y = random.randint(2, 19) * 30
    return speed, score, tails

def update_tail_pos(tails, tail, last):
    last_ctr = [tails[tail].x, tails[tail].y]
    tails[tail].x = last[0]
    tails[tail].y = last[1]
    return last_ctr
def collision(snake, tails):
    for i in range(2, len(tails)):
        if tails[i].x == snake.x and tails[i].y == snake.y:
            print(1)

    return True
food_x = random.randint(1, 19) * 30
food_y = random.randint(2, 19) * 30
food = box(RED, food_x, food_y)

snake = box(BLUE, 300, 330)

score = 0
speed = 2
tails = []
run = True
while run:
    window.fill(SILVER)
    if len(tails) > 0:
        last = [snake.x, snake.y]
        for tail in range(len(tails)):
            last = update_tail_pos(tails, tail, last)
            pygame.draw.rect(window, tails[tail].color, (tails[tail].x, tails[tail].y, BOX_SIZE, BOX_SIZE))

    pos = move(snake, direction)
    snake.x = pos[0]
    snake.y = pos[1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction[2] == False:
                direction = [True, False, False, False]
            elif event.key == pygame.K_UP and direction[3] == False:
                direction = [False, True, False, False]
            elif event.key == pygame.K_RIGHT and direction[0] == False:
                direction = [False, False, True, False]
            elif event.key == pygame.K_DOWN and direction[1] == False:
                direction = [False, False, False, True]



    pygame.draw.rect(window, snake.color, (snake.x, snake.y, BOX_SIZE, BOX_SIZE))

    pygame.draw.rect(window, food.color, (food.x, food.y, BOX_SIZE, BOX_SIZE))

    speed, score, tails = eat(snake, food, speed, score, tails, BLUE)
    run = collision(snake, tails)
    draw_grid(WIDTH, HEIGHT, WHITE)
    text = "SCORE: " + str(score)
    score_text = my_font.render(text, 1, BLACK)
    window.blit(score_text, (230, 0))

    clock.tick(speed)
    pygame.display.update()

# BY REYES EUGENE