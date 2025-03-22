# conda activate allpy310

# Частотный анализ текстов

from collections import Counter
import re

def clean_text(text):
    """Очищает текст от пунктуации и приводит к нижнему регистру."""
    text = re.sub(r'[^\w\s]', '', text)  # Убираем пунктуацию
    return text.lower()

def analyze_text(file_path):
    """Читает файл и анализирует частоту слов."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        cleaned_text = clean_text(text)
        words = cleaned_text.split()
        word_count = Counter(words)
        return word_count
    except FileNotFoundError:
        print("Файл не найден.")
        return None

def display_top_words(word_count, top_n=10):
    """Выводит топ N самых частых слов."""
    print(f"\nТоп {top_n} самых частых слов:")
    for word, count in word_count.most_common(top_n):
        print(f"{word}: {count}")

if __name__ == "__main__":
    print("Программа: Анализатор частоты слов")
    file_path = input("Введите путь к текстовому файлу: ").strip()
    word_count = analyze_text(file_path)
    if word_count:
        top_n = input("Сколько самых частых слов вывести? (По умолчанию: 10): ").strip()
        top_n = int(top_n) if top_n.isdigit() else 10
        display_top_words(word_count, top_n)

'''
Программа: Анализатор частоты слов
Введите путь к текстовому файлу: D:\TXT_base\python_examples_base.txt
Сколько самых частых слов вывести? (По умолчанию: 10): 50

Топ 10 самых частых слов:
с: 181
и: 165
для: 157
import: 152
в: 151
2: 101
1: 93
in: 81
for: 77
на: 73
'''