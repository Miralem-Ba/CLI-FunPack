import pygame
import random
import time

pygame.init()

# Einstellungen
WIDTH, HEIGHT = 1600, 1600
GRID_SIZE = 4
TILE_SIZE = WIDTH // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (128, 0, 128), (0, 255, 255), (255, 192, 203)]
COLORS *= 2
random.shuffle(COLORS)

