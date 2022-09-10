import pygame
import sys

from pygame import draw
from pygame.surface import Surface
from pygame.time import Clock

pygame.init()
size = width, height = 640, 480
speed = [2, 2]
black = 0, 0, 0
white = 255, 255, 255
screen = pygame.display.set_mode(size)

ball = Surface((64, 64))
draw.circle(ball, white, (32, 32), 30, 2)

clock = Clock()

ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    clock.tick(60)
