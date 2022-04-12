import pygame
import sys
import random
import math
pygame.init()
pygame.font.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("PONG")

running = True

WHITE = (255, 255, 255)
BLUE = (50, 115, 255)
RED = (255, 0, 0)

font = pygame.font.Font("Font.ttf", 13)

def randc(a, b):
    rnd = random.randrange(0, 2)
    if rnd == 1:
        return a
    else:
        return b

p1Rect = pygame.Rect(WIDTH - 18, HEIGHT/2-40, 9, 80)
p1Score = 0
p2Rect = pygame.Rect(9, HEIGHT/2-40, 9, 80)
p2Score = 0
p1velY = 0
p2velY = 0

ballRect = pygame.Rect(WIDTH/2-6, HEIGHT/2-6, 12, 12)
ballColor = WHITE
ballVelX = randc(-3.5, 3.5)
ballVelY = randc(-3.5, 3.5)
nbvx = bellVelX
nbvy = ballVelY

while running:
    screen.fill((0, 0, 0))

    p1ScoreT = font.render(str(p1Score), False, (255, 255, 255))
    p2ScoreT = font.render(str(p2Score), False, (255, 255, 255))

    pygame.draw.rect(screen, (255, 255, 255), p1Rect)
    pygame.draw.rect(screen, (255, 255, 255), p2Rect)
    pygame.draw.rect(screen, ballColor, ballRect)

    screen.blit(p1ScoreT, (60, 20))
    screen.blit(p2ScoreT, (WIDTH-60, 20))

    if ballRect.x < 0: 
        ballVelX = -ballVelX
        p2Score += 1
    if ballRect.x > WIDTH-12: 
        ballVelX = -ballVelX
        p1Score += 1
    if ballRect.y < 0: ballVelY = -ballVelY
    if ballRect.y > HEIGHT-12: ballVelY = -ballVelY

    if p1Rect.y < 9: p1Rect.y = 9
    if p1Rect.y > HEIGHT-9-80: p1Rect.y = HEIGHT-9-80
    if p2Rect.y < 9: p2Rect.y = 9
    if p2Rect.y > HEIGHT-9-80: p2Rect.y = HEIGHT-9-80

    if p1Rect.colliderect(ballRect):
        ballVelX = -ballVelX
        ballColor = BLUE
    elif p2Rect.colliderect(ballRect):
        ballVelX = -ballVelX
        ballColor = RED

    p1Rect.y += p1velY
    p2Rect.y += p2velY

    ballRect.x += ballVelX
    ballRect.y += ballVelY

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP:
                p1velY = -4
            if event.key == pygame.K_DOWN:
                p1velY = 4

            if event.key == pygame.K_w:
                p2velY = -4
            if event.key == pygame.K_s:
                p2velY = 4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                p1velY = 0
            if event.key == pygame.K_DOWN:
                p1velY = 0

            if event.key == pygame.K_w:
                p2velY = 0
            if event.key == pygame.K_s:
                p2velY = 0

    pygame.display.update()
    clock.tick(60)