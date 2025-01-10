import math

def calculate(expression):
    """Вычисление заданного выражения."""
    try:
        # Подключение встроенных математических функций
        result = eval(expression, {"__builtins__": None}, {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "sqrt": math.sqrt,
            "log": math.log,
            "pi": math.pi,
            "e": math.e,
            "pow": math.pow,
            "abs": abs,
        })
        return result
    except Exception as e:
        return f"Ошибка: {e}"

if __name__ == "__main__":
    print("Калькулятор")
    print("Введите математическое выражение для расчета (или 'выход'/'end' для завершения):")

    while True:
        expression = input(">>> ").strip()
        if expression.lower() == "выход" or expression.lower() == "end":
            print("До свидания!")
            break
        result = calculate(expression)
        print(f"Результат: {result}")