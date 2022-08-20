import pygame
import sys
import time
import random

RESOLUTION = (1280, 720)
pygame.init()
SCREEN = pygame.display.set_mode(RESOLUTION)
FONT = pygame.font.Font('freesansbold.ttf', 64)
BG = pygame.image.load("bg.png")
PLAYER = pygame.Rect(590, 310, 50, 50)
P_H = random.randrange(200, 520)
PIPE = (pygame.Rect(1280, 0, 100, P_H), pygame.Rect(1280, P_H+200, 100, 720-(P_H+200)), False)
PIPES = [PIPE]
GAME = True
RESULT = 0

while True:
    SCREEN.blit(BG, (0, 0))
    # Handling events
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(1)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if GAME == True:
                    PLAYER.y -= 80
                # Handling game restart
                else:
                    PLAYER = pygame.Rect(590, 310, 50, 50)
                    P_H = random.randrange(200, 520)
                    PIPES = []
                    PIPES.append((pygame.Rect(1280, 0, 100, P_H), pygame.Rect(1280, P_H+200, 100, 720-(P_H+200)), False))
                    RESULT = 0
                    GAME = True

    # Handling game
    if GAME:
        time.sleep(0.004)
        if PLAYER.y != 670:
            PLAYER.y += 1
        else:
            RESULT = 0
            GAME = False
        
        # Handling adding pipes
        # Second pipe
        if len(PIPES) == 1:
            if PIPES[0][0].x == 980:
                P_H = random.randrange(200, 520)
                PIPES.append((pygame.Rect(1280, 0, 100, P_H), pygame.Rect(1280, P_H+200, 100, 720-(P_H+200)), False))
        # Any other pipe
        if len(PIPES) >= 2:
            if 1280 - PIPES[len(PIPES)-1][0].x == 300:
                P_H = random.randrange(200, 520)
                PIPES.append((pygame.Rect(1280, 0, 100, P_H), pygame.Rect(1280, P_H+200, 100, 720-(P_H+200)), False))
        
        # Handling deleting first pipes
        if PIPES[0][0].x == -100:
            PIPES.pop(0)

        # Handling pipe moving
        for pipe in PIPES:
            for part in pipe:
                if type(part) == pygame.Rect:
                    part.x -=1
        
        # Handling pipe colision
        for pipe in PIPES:
            if (PLAYER.x + PLAYER.w) in range(pipe[0].x, pipe[0].x + pipe[0].w):
                if PLAYER.y in range(pipe[0].y, pipe[0].y + pipe[0].h):
                    GAME = False
            if (PLAYER.x + PLAYER.w) in range(pipe[1].x, pipe[1].x + pipe[1].w):
                if (PLAYER.y + PLAYER.h) in range(pipe[1].y, pipe[1].y + pipe[1].h):
                    GAME = False
            # Handling result counter (in colision loop cause it is same loop)
            if (PLAYER.x + PLAYER.w) > (pipe[0].x + pipe[0].w):
                if pipe[2] == False:
                    temp = list(PIPES[PIPES.index(pipe)])
                    temp[2] = True
                    PIPES[PIPES.index(pipe)] = tuple(temp)
                    RESULT += 1

        # Displaying background
        SCREEN.blit(BG, (0, 0)) 
        # Displaying player
        pygame.draw.rect(SCREEN, (255, 255, 255), PLAYER)
        # Displaying pipes
        for pipe in PIPES:
            for part in pipe:
                if type(part) == pygame.Rect:
                    pygame.draw.rect(SCREEN, (0, 240, 0), part)
        # Displaying resoult
        TEXT = FONT.render(str(RESULT), True, (0,0,0), (255,255,255))
        TRECT = TEXT.get_rect()
        TRECT.center = (640, 100)
        SCREEN.blit(TEXT, TRECT)
        pygame.display.flip()