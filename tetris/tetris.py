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

# Formen
SHAPES = [
    [[1, 1, 1, 1]],  # I-Form
    [[1, 1], [1, 1]],  # O-Form
    [[0, 1, 0], [1, 1, 1]],  # T-Form
    [[1, 1, 0], [0, 1, 1]],  # S-Form
    [[0, 1, 1], [1, 1, 0]],  # Z-Form
    [[1, 0, 0], [1, 1, 1]],  # J-Form
    [[0, 0, 1], [1, 1, 1]],  # L-Form
]

# Initialisierung des Spielfelds
field = [[BLACK for _ in range(COLUMNS)] for _ in range(ROWS)]

# Fenster erstellen
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

# Zufällige Form generieren
def new_piece():
    shape = random.choice(SHAPES)
    color = random.choice(COLORS)
    return {'shape': shape, 'color': color, 'x': COLUMNS // 2 - len(shape[0]) // 2, 'y': 0}

