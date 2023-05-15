#importing required modules
import pygame
import random
import sys

# Initialising the modules in pygame
pygame.init()
#setting frames per second for speed
FPSCLOCK = pygame.time.Clock()
FPS=60
#creating game display
window = pygame.display.set_mode((500, 700))  
bgimage = pygame.image.load('save3 (8).png')

# bird
bimage = pygame.image.load('bird (1).png')
b_x = 50
b_y = 300
b_y_change = 0

#obstacle
OBSTACLE_WIDTH = 70
OBSTACLE_HEIGHT = random.randint(150,420)
OBSTACLE_COLOR = (253, 0, 253)
OBSTACE_X_CHANGE = -4
obstacle_x = 480

def displaybird(x, y):
    window.blit(bimage, (x, y))

def displayobstacle(height):
    pygame.draw.rect(window, OBSTACLE_COLOR, (obstacle_x, 0, OBSTACLE_WIDTH, height))
    bottom_obstacle_height = 550 - height - 200
    pygame.draw.rect(window, OBSTACLE_COLOR, (obstacle_x, 500-bottom_obstacle_height, OBSTACLE_WIDTH, 500))


def collisiondetection (obstacle_x, obstacle_height, bird_y, bottom_obstacle_height):
    if obstacle_x >= 50 and obstacle_x <= (50 + 64):
        if bird_y <= obstacle_height or bird_y >= (bottom_obstacle_height - 64):
            return True
    return False


score = 0
SCORE_FONT = pygame.font.Font('freesansbold.ttf', 32)

def scoredisplay(score):
    display = SCORE_FONT.render(f"Score: {score}", True, (255,255,255))
    window.blit(display, (10, 10))

# Start screen
startFont = pygame.font.Font('freesansbold.ttf', 32)
def start():
    display = startFont.render(f"PRESS SPACE BAR TO START GAME", True, (0,0,0))
    window.blit(display, (20, 200))
    pygame.display.update()

# GAME OVER SCREEN
score_list = [0]
gameoverfont1 = pygame.font.Font('freesansbold.ttf', 64)
gameoverfont2 = pygame.font.Font('freesansbold.ttf', 32)
def gameover():
    #maximum score
    maximum = max(score_list)
    d1 = gameoverfont1.render(f"GAME OVER!!", True, (200,35,35))
    window.blit(d1, (50, 300))
    #current and max score
    d2 = gameoverfont2.render(f"SCORE: {score} MAX SCORE: {maximum}", True, (255, 255, 255))
    window.blit(d2, (50, 400))
    #High score
    if score == maximum:
        d3 = gameoverfont2.render(f"  NEW HIGH SCORE", True, (200,35,35))
        window.blit(d3, (80, 100))

run = True
wait = True
collision = False
while run:
    window.fill((0, 0, 0))
    # display the background image
    window.blit(bgimage, (0, 0))
    while wait:
        if collision:
            gameover()
            start()
        else:
            start()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    score = 0
                    b_y = 300
                    obstacle_x = 500
                    #  to exit out of the while loop
                    wait = False

            if event.type == pygame.QUIT:
                wait = False
                run = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #  if you press spacebar you will move up
                b_y_change = -6

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                # when u release space bar you will move down automatically
                b_y_change = 3
    b_y += b_y_change
    # setting boundaries for the birds movement
    if b_y <= 0:
        b_y = 0
    if b_y >= 571:
        b_y = 571

    obstacle_x += OBSTACE_X_CHANGE

    # COLLISIOcollision
    collision = collisiondetection(obstacle_x, OBSTACLE_HEIGHT, b_y, OBSTACLE_HEIGHT + 150)

    if collision:
        score_list.append(score)
        wait = True

    #obstacle generation
    if obstacle_x <= -10:
        obstacle_x = 500
        OBSTACLE_HEIGHT = random.randint(150, 420)
        score += 1
    # displaying the obstacle,bird,score
    displayobstacle(OBSTACLE_HEIGHT)
    displaybird(b_x, b_y)
    scoredisplay(score)
    # Update the display after each iteration of the while loop
    pygame.display.update()
    FPSCLOCK.tick(FPS)
