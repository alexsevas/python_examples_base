# conda activate allpy310
# Анимация шаровой молнии

import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение размеров и цветов экрана
screen_width = 800
screen_height = 600
background_color = (30, 30, 30)

# Создание экрана и окна
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Шаровая молния")

# Шаровая молния
class LightningBall:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Генерация случайной шаровой молнии
def generate_lightning_ball():
    x = random.randint(50, screen_width - 50)
    y = random.randint(50, screen_height - 50)
    radius = random.randint(20, 50)
    color = (random.randint(200, 255), random.randint(200, 255), random.randint(50, 100))
    return LightningBall(x, y, radius, color)

# Основной цикл программы
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(background_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отрисовка шаровой молнии
    lightning_ball = generate_lightning_ball()
    lightning_ball.draw()

    # Обновление дисплея и задание FPS
    pygame.display.flip()
    clock.tick(5)

# Завершение работы Pygame
pygame.quit()
