# pip install pymongo

# conda activate allpy310

from pymongo import MongoClient

# Подключаемся к серверу MongoDB (по умолчанию это localhost:27017)
client = MongoClient('mongodb://localhost:27017/')

# Создаем или подключаемся к существующей базе данных
db = client.my_database

# Создаем или подключаемся к коллекции
collection = db.my_collection

# Добавляем документ в коллекцию
data = {"name": "Alice", "age": 30, "email": "alice@example.com"}
collection.insert_one(data)

print("Document inserted!")