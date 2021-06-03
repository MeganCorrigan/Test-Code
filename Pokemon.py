import pygame
import Configurations

pygame.init()

screen = pygame.display.set_mode((600, 400))

pygame.display.set_caption("Pokemon Clone")

while True:
    screen.fill(Configurations.BLACK)
    pygame.display.flip()