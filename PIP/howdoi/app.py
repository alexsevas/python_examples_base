# ENV allpy310

# pip install howdoi

from howdoi import howdoi

# Формируем запрос
query = "reverse a list in python"

# Формируем параметры запроса, добавляя необходимые ключи
params = {
    'query': 'reverse a list in python',
    'all': False,
    'num_answers': 1,
    'pos': 1,
    'search_engine': 'yandex',  # Явно указываем поисковую систему
    'explain': False  # Предполагаемое значение для 'explain'
}

# Получаем ответ
answer = howdoi.howdoi(params)

print(f"Вопрос: Как перевернуть список в Python?")
print("Ответ:")
print(answer)