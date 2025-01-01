# Калькулятор индекса массы тела человека

def calculate_bmi(weight, height):
    """Вычисляет индекс массы тела (ИМТ)."""
    try:
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        print("Рост не может быть равен нулю.")
        return None


def interpret_bmi(bmi):
    """Интерпретирует значение ИМТ."""
    if bmi < 18.5:
        return "Недостаточный вес"
    elif 18.5 <= bmi < 24.9:
        return "Нормальный вес"
    elif 25 <= bmi < 29.9:
        return "Избыточный вес"
    else:
        return "Ожирение"


if __name__ == "__main__":
    print("Программа: Калькулятор ИМТ")
    while True:
        print("\nМеню:")
        print("1. Рассчитать ИМТ")
        print("2. Выйти")
        choice = input("Выберите действие (1-2): ").strip()

        if choice == "1":
            try:
                weight = float(input("Введите вес (кг): ").strip())
                height = float(input("Введите рост (м): ").strip())
                bmi = calculate_bmi(weight, height)
                if bmi is not None:
                    category = interpret_bmi(bmi)
                    print(f"Ваш ИМТ: {bmi}")
                    print(f"Категория: {category}")
            except ValueError:
                print("Пожалуйста, введите корректные числовые значения.")
        elif choice == "2":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
