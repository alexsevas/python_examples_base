# conda activate allpy310, py310test

import os
import random
import time

# ASCII-анимация «Матрицы» с медленными и плотными столбиками
def matrix_rain(width=80, height=24):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()'
    drops = [random.randint(-height, 0) for _ in range(width)]

    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            output = [' ' * width for _ in range(height)]

            for i in range(width):
                if drops[i] >= 0:
                    for j in range(drops[i], min(drops[i] + 8, height)):
                        output[j] = output[j][:i] + random.choice(chars) + output[j][i + 1:]
                drops[i] += 1
                if drops[i] > height and random.random() > 0.8:
                    drops[i] = random.randint(-10, 0)

            print('\n'.join(output))
            time.sleep(0.1)
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Animation stopped.")

matrix_rain()
