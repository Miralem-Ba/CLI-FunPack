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

# Fenster erstellen
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Game")

tiles = []
revealed = []
selected = []

for i in range(GRID_SIZE):
    row = []
    reveal_row = []
    for j in range(GRID_SIZE):
        row.append(COLORS.pop())
        reveal_row.append(False)
    tiles.append(row)
    revealed.append(reveal_row)

def draw_tiles():
    win.fill(WHITE)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            rect = pygame.Rect(j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if revealed[i][j]:
                pygame.draw.rect(win, tiles[i][j], rect)
            else:
                pygame.draw.rect(win, BLACK, rect)
            pygame.draw.rect(win, WHITE, rect, 2)
    pygame.display.update()

def check_match():
    if len(selected) == 2:
        r1, c1 = selected[0]
        r2, c2 = selected[1]
        if tiles[r1][c1] == tiles[r2][c2]:
            return True
        else:
            return False

running = True
while running:
    draw_tiles()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and len(selected) < 2:
            x, y = event.pos
            row, col = y // TILE_SIZE, x // TILE_SIZE
            if not revealed[row][col]:
                revealed[row][col] = True
                selected.append((row, col))
    
    if len(selected) == 2:
        draw_tiles()
        pygame.time.delay(1000)
        if not check_match():
            r1, c1 = selected[0]
            r2, c2 = selected[1]
            revealed[r1][c1] = False
            revealed[r2][c2] = False
        selected.clear()
    
pygame.quit()
