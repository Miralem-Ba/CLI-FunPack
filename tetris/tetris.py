import pygame
import random

pygame.init()

# Spielfeldgröße
WIDTH, HEIGHT = 1300, 1600
BLOCK_SIZE = 50
COLUMNS, ROWS = WIDTH // BLOCK_SIZE, HEIGHT // BLOCK_SIZE

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [(0, 255, 255), (0, 0, 255), (255, 165, 0), (255, 255, 0), (0, 255, 0), (128, 0, 128), (255, 0, 0)]

