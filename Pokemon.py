import pygame

pygame.init()

screen = pygame.display.set_mode(600, 400)

pygame.display.set_caption("Pokemon Clone")

screen.fill(config.BLACK)

pygame.display.flip()