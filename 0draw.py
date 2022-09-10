import pygame

from pygame import draw
from pygame.surface import Surface

pygame.init()
size = width, height = 640, 480
black = 0, 0, 0
white = 255, 255, 255
screen = pygame.display.set_mode(size)

# https://www.pygame.org/docs/ref/draw.html
ball = Surface((64, 64))
draw.circle(ball, white, (32, 32), 30, 2)
ball_rect = ball.get_rect()
#ball = pygame.image.load("intro_ball.gif")

screen.fill(black)
screen.blit(ball, ball_rect)
pygame.display.flip()

input("Press enter to quit")