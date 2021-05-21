import pygame
import Configurations

from game import Game

pygame.init()

screen = pygame.display.set_mode(600, 400)

pygame.display.set_caption("Pokemon Clone")

game = Game(screen)

while True:
    screen.fill(config.BLACK)
    pygame.display.flip()