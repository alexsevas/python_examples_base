from pywebio.input import input, FLOAT
from pywebio.output import put_text

def calculate_square_root():
    number = input("Введите число для извлечения квадратного корня:", type=FLOAT)
    square_root = number ** 0.5
    put_text(f"Квадратный корень из {number}: {square_root:.2f}")

if __name__ == "__main__":
    calculate_square_root()