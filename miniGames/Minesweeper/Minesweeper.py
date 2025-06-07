#conda activate allpy310

'''
Простая версию игры "Сапёр" с размером поля 5x5 и 5 бомбами. Игрок должен вводить координаты клетки поля, и если там нет
бомбы, то открывается число, указывающее, сколько бомб находится рядом с этой клеткой. Когда игрок попадает на бомбу,
игра завершается.
'''

import random

def create_board(rows, cols, bombs):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]

    for _ in range(bombs):
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)

        while board[row][col] == '*':
            row = random.randint(0, rows - 1)
            col = random.randint(0, cols - 1)

        board[row][col] = '*'

    return board

def print_board(board):
    for row in board:
        print(" ".join(row))

def count_bombs(row, col, board):
    count = 0
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if r >= 0 and r < len(board) and c >= 0 and c < len(board[0]):
                if board[r][c] == '*':
                    count += 1
    return count

def main():
    rows = 5
    cols = 5
    bombs = 5

    board = create_board(rows, cols, bombs)

    print_board(board)

    while True:
        user_row = int(input("Enter row: "))
        user_col = int(input("Enter column: "))

        if board[user_row][user_col] == '*':
            print("Game over! You hit a bomb.")
            break

        bombs_near = count_bombs(user_row, user_col, board)
        board[user_row][user_col] = str(bombs_near)

        print_board(board)

if __name__ == "__main__":
    main()
