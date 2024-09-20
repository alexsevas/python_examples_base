# pip install pygame
# conda activate all2py310

import pygame
import sys
import random

pygame.init()

# Определение размеров и цветов
CELL_SIZE = 20
GRID_WIDTH = 20
GRID_HEIGHT = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Инициализация экрана
screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
pygame.display.set_caption("Snake")

# Определение змеи и ее движения
snake = [(2, 2), (3, 2), (4, 2)]
snake_dir = (1, 0)

food = (6, 6)

def move_snake(snake, snake_dir):
    head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake.insert(0, head)
    snake.pop()

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, RED, pygame.Rect(food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def random_food(snake):
    while True:
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        if (x, y) not in snake:
            return (x, y)

def game_over():
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over", True, WHITE)
    screen.blit(text, (GRID_WIDTH * CELL_SIZE / 2 - text.get_width() / 2, GRID_HEIGHT * CELL_SIZE / 2 - text.get_height() / 2))
    pygame.display.flip()
    pygame.time.wait(300)

clock = pygame.time.Clock()

while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, 1):
                snake_dir = (0, -1)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -1):
                snake_dir = (0, 1)
            elif event.key == pygame.K_LEFT and snake_dir != (1, 0):
                snake_dir = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-1, 0):
                snake_dir = (1, 0)

    # Обновление змеи
    move_snake(snake, snake_dir)

    # Проверка столкновений с границами или самим собой
    if (snake[0][0] < 0 or snake[0][0] >= GRID_WIDTH or
        snake[0][1] < 0 or snake[0][1] >= GRID_HEIGHT or
        snake[0] in snake[1:]):
        game_over()
        snake = [(2, 2), (3, 2), (4, 2)]
        snake_dir = (1, 0)
        food = random_food(snake)

    # Проверка столкновения с едой
    if snake[0] == food:
        food = random_food(snake)
        snake.append(snake[-1])

    # Отрисовка экрана
    screen.fill((0, 0, 0))
    draw_snake(snake)
    draw_food(food)
    pygame.display.flip()

    clock.tick(10)