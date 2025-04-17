import pygame
import random
import sys

# Game settings
WIDTH, HEIGHT = 600, 600
TILE_SIZE = 40
ROWS, COLS = HEIGHT // TILE_SIZE, WIDTH // TILE_SIZE
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
GREEN = (0, 255, 0)
RED = (200, 50, 50)
BLACK = (0, 0, 0)

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Labyrinth of Abarat (Test Version)")
clock = pygame.time.Clock()

# Player, goal, and enemy positions
player_pos = [0, 0]
books = [[random.randint(1, COLS - 2), random.randint(1, ROWS - 2)] for _ in range(6)]
enemies = [[random.randint(1, COLS - 2), random.randint(1, ROWS - 2)] for _ in range(3)]

score = 0

def draw_grid():
    for x in range(0, WIDTH, TILE_SIZE):
        pygame.draw.line(win, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILE_SIZE):
        pygame.draw.line(win, BLACK, (0, y), (WIDTH, y))

def draw():
    win.fill(WHITE)
    draw_grid()

    pygame.draw.rect(win, BLUE, (*[i * TILE_SIZE for i in player_pos], TILE_SIZE, TILE_SIZE))
    for b in books:
        pygame.draw.rect(win, GREEN, (*[i * TILE_SIZE for i in b], TILE_SIZE, TILE_SIZE))
    for e in enemies:
        pygame.draw.rect(win, RED, (*[i * TILE_SIZE for i in e], TILE_SIZE, TILE_SIZE))

    pygame.display.update()

def move_enemies():
    for e in enemies:
        direction = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
        e[0] = max(0, min(COLS - 1, e[0] + direction[0]))
        e[1] = max(0, min(ROWS - 1, e[1] + direction[1]))

def check_collision():
    global score
    for b in books[:]:
        if player_pos == b:
            books.remove(b)
            score += 1
    for e in enemies:
        if player_pos == e:
            return True
    return False

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos[1] = max(0, player_pos[1] - 1)
    if keys[pygame.K_s]:
        player_pos[1] = min(ROWS - 1, player_pos[1] + 1)
    if keys[pygame.K_a]:
        player_pos[0] = max(0, player_pos[0] - 1)
    if keys[pygame.K_d]:
        player_pos[0] = min(COLS - 1, player_pos[0] + 1)

    move_enemies()
    if check_collision():
        print("You were caught! Game Over.")
        running = False
    if score == 6:
        print("You collected all the books! Victory!")
        running = False

    draw()
