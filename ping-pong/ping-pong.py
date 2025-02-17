import pygame
import random

# Initialisieren von Pygame
pygame.init()

# Spielfeldgrößen definieren
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Farben definieren
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Schläger-Eigenschaften
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_RADIUS = 8

# Paddle Positionen
left_paddle = pygame.Rect(30, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 40, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH//2, HEIGHT//2, BALL_RADIUS, BALL_RADIUS)

# Geschwindigkeit
paddle_speed = 7
ball_speed_x = random.choice([-4, 4])
ball_speed_y = random.choice([-4, 4])

# Punkte
score_left = 0
score_right = 0

# Schriftart
font = pygame.font.Font(None, 40)

running = True
while running:
    pygame.time.delay(20)
    screen.fill(BLACK)
    
    # Event-Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Steuerung
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= paddle_speed
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += paddle_speed
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += paddle_speed
    
    # Ballbewegung
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # Kollision mit Wänden
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    
    # Kollision mit Schlägern
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x *= -1
    
    # Punkte zählen
    if ball.left <= 0:
        score_right += 1
        ball.x, ball.y = WIDTH//2, HEIGHT//2
        ball_speed_x *= random.choice([-1, 1])
    if ball.right >= WIDTH:
        score_left += 1
        ball.x, ball.y = WIDTH//2, HEIGHT//2
        ball_speed_x *= random.choice([-1, 1])
    
    # Zeichnen
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))
    
    # Punkte anzeigen
    score_text = font.render(f"{score_left}  -  {score_right}", True, WHITE)
    screen.blit(score_text, (WIDTH//2 - 30, 20))
    
    pygame.display.update()
    
pygame.quit()
