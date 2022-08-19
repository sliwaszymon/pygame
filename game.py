import pygame
import sys
import time
import random

RESOLUTION = (1280, 720)
pygame.init()
SCREEN = pygame.display.set_mode(RESOLUTION)
PLAYER = pygame.Rect(590, 310, 50, 50)
P_H = random.randrange(200, 520)
PIPE = (pygame.Rect(1280, 0, 100, P_H), pygame.Rect(1280, P_H+200, 100, 720-(P_H+200)))
PIPES = [PIPE]
GAME = True

while True:
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
                    PIPES.append((pygame.Rect(1280, 0, 100, P_H), pygame.Rect(1280, P_H+200, 100, 720-(P_H+200))))
                    GAME = True

    # Handling game
    if GAME:
        time.sleep(0.004)
        if PLAYER.y != 670:
            PLAYER.y += 1
        else:
            GAME = False
        
        if len(PIPES) == 1:
            if PIPES[0][0].x == 980:
                P_H = random.randrange(200, 520)
                PIPES.append((pygame.Rect(1280, 0, 100, P_H), pygame.Rect(1280, P_H+200, 100, 720-(P_H+200))))
        
        if len(PIPES) >= 2:
            if 1280 - PIPES[len(PIPES)-1][0].x == 300:
                P_H = random.randrange(200, 520)
                PIPES.append((pygame.Rect(1280, 0, 100, P_H), pygame.Rect(1280, P_H+200, 100, 720-(P_H+200))))
        
        if PIPES[0][0].x == -100:
            PIPES.pop(0)

        for pipe in PIPES:
            for part in pipe:
                part.x -=1
        
        # Handling pipe colision
        for pipe in PIPES:
            if (PLAYER.x + PLAYER.h) in range(pipe[0].x, pipe[0].x + pipe[0].w):
                if PLAYER.y in range(pipe[0].y, pipe[0].y + pipe[0].h):
                    GAME = False
            if (PLAYER.x + PLAYER.h) in range(pipe[1].x, pipe[1].x + pipe[1].w):
                if (PLAYER.y + PLAYER.h) in range(pipe[1].y, pipe[1].y + pipe[1].h):
                    GAME = False

        SCREEN.fill((0,0,0))
        pygame.draw.rect(SCREEN, (128, 128, 128), PLAYER)
        for pipe in PIPES:
            for part in pipe:
                pygame.draw.rect(SCREEN, (0, 240, 0), part)
        pygame.display.flip()