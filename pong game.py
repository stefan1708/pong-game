import pygame
import random

# initializare Pygame
pygame.init()

# prgatire ecran
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# culori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# proptietati bila
BALL_RADIUS = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = 5 * random.choice((1, -1))
ball_dy = 5 * random.choice((1, -1))

# proprietati padele
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 7
left_paddle_y = (HEIGHT - PADDLE_HEIGHT) // 2
right_paddle_y = (HEIGHT - PADDLE_HEIGHT) // 2

# scor
left_score = 0
right_score = 0

# bucla main a jocului
clock = pygame.time.Clock()
running = True
while running:
    # event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # miscarea padelelor
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle_y < HEIGHT - PADDLE_HEIGHT:
        left_paddle_y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle_y < HEIGHT - PADDLE_HEIGHT:
        right_paddle_y += PADDLE_SPEED

    # miscarea bilei
    ball_x += ball_dx
    ball_y += ball_dy

    # colizie bila in portiunile sus jos
    if ball_y <= BALL_RADIUS or ball_y >= HEIGHT - BALL_RADIUS:
        ball_dy *= -1

    # colizie bila in padele
    if (ball_x <= PADDLE_WIDTH and left_paddle_y <= ball_y <= left_paddle_y + PADDLE_HEIGHT) or \
            (ball_x >= WIDTH - PADDLE_WIDTH and right_paddle_y <= ball_y <= right_paddle_y + PADDLE_HEIGHT):
        ball_dx *= -1

    # bila in afara limitelor
    if ball_x <= 0:
        right_score += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
    elif ball_x >= WIDTH:
        left_score += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2

    # curatare ecran
    screen.fill(BLACK)

    # desen padele
    pygame.draw.rect(screen, WHITE, pygame.Rect(0, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, pygame.Rect(WIDTH - PADDLE_WIDTH, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # desen bila
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)

    # scoreboard
    font = pygame.font.Font(None, 36)
    left_score_text = font.render(str(left_score), True, WHITE)
    right_score_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_score_text, (WIDTH // 4, 50))
    screen.blit(right_score_text, (3 * WIDTH // 4, 50))

    # update display
    pygame.display.flip()

    # frame rate
    clock.tick(60)

# iesire pygame
pygame.quit()
