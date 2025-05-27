import pygame
import sys
import json
import os
import random
from datetime import datetime

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
FPS = 10

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Загрузка результатов из файла
def load_results():
    if os.path.exists("results.json"):
        with open("results.json", "r") as f:
            return json.load(f)
    return {}

# Сохранение результатов в файл
def save_results(results):
    with open("results.json", "w") as f:
        json.dump(results, f)

# Основная игра
def game():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Змейка")
    clock = pygame.time.Clock()

    # Змейка
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = (CELL_SIZE, 0)
    food = (random.randint(0, (WIDTH // CELL_SIZE - 1)) * CELL_SIZE,
            random.randint(0, (HEIGHT // CELL_SIZE - 1)) * CELL_SIZE)

    # Игровой цикл
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and direction != (0, CELL_SIZE):
                    direction = (0, -CELL_SIZE)
                elif event.key == pygame.K_s and direction != (0, -CELL_SIZE):
                    direction = (0, CELL_SIZE)
                elif event.key == pygame.K_a and direction != (CELL_SIZE, 0):
                    direction = (-CELL_SIZE, 0)
                elif event.key == pygame.K_d and direction != (-CELL_SIZE, 0):
                    direction = (CELL_SIZE, 0)

        # Движение
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, new_head)

        # Проверка на еду
        if snake[0] == food:
            food = (random.randint(0, (WIDTH // CELL_SIZE - 1)) * CELL_SIZE,
                    random.randint(0, (HEIGHT // CELL_SIZE - 1)) * CELL_SIZE)
        else:
            snake.pop()

        # Проверка на столкновение
        if (snake[0][0] < 0 or snake[0][0] >= WIDTH or
            snake[0][1] < 0 or snake[0][1] >= HEIGHT or
            snake[0] in snake[1:]):
            running = False
            break

        # Отрисовка
        screen.fill(BLACK)
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))
        pygame.display.flip()
        clock.tick(FPS)

    return len(snake) - 1  # Уровень (длина змейки - 1)

# Отображение таблицы результатов
def show_results(results):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Таблица результатов")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 16)

    # Сортировка результатов по убыванию уровня
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        text = font.render("Таблица результатов:", True, BLACK)
        screen.blit(text, (10, 10))

        for i, (name, level) in enumerate(sorted_results):
            text = font.render(f"{i+1}. {name}: Уровень {level}", True, BLACK)
            screen.blit(text, (10, 50 + i * 30))

        pygame.display.flip()
        clock.tick(FPS)

# Основная функция
def main():
    results = load_results()
    name = input("Введите ваше имя: ")
    level = game()
    print(f"Вы дошли до уровня {level}")

    # Обновление результатов
    if name in results:
        if level > results[name]:
            results[name] = level
    else:
        results[name] = level

    save_results(results)
    show_results(results)

if __name__ == "__main__":
    main()