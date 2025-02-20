# ENV allpy310
# pip install faker

from faker import Faker

# Создаем объект Faker. Можно указать язык/локаль для генерации данных, например, 'ru_RU' для русскоязычных данных.
fake = Faker()

# Генерируем и выводим фиктивные данные
print("Фиктивные данные пользователя:")

for _ in range(5):  # Генерируем данные для 5 пользователей
    name = fake.name()  # Имя
    address = fake.address()  # Адрес
    email = fake.email()  # Электронная почта
    job = fake.job()  # Профессия
    date_of_birth = fake.date_of_birth()  # Дата рождения

    # Выводим сгенерированные данные
    print(f"Имя: {name}, Дата рождения: {date_of_birth}, Профессия: {job}, Email: {email}, Адрес: {address}\n")

# Генерация текста на "рыбном" языке
lorem_text = fake.text()
print("Пример текста на 'рыбном' языке:")
print(lorem_text)
