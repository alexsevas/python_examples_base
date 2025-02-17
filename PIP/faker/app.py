# ENV allpy310
# pip install faker

from faker import Faker

fake = Faker()

# Генерация данных
print(fake.name())      # Случайное имя
print(fake.address())   # Случайный адрес
print(fake.email())     # Случайный email
