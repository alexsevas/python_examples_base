# conda activate allpy310
# pip install argostranslate pdfplumber docx2txt

'''
Локальный офлайн-переводчик документов и текста (PDF, DOCX, TXT):
-️ Перевод технических документов, статей, инструкций
- Работа в оффлайн-средах (военные, научные проекты, закрытые офисы)
- Перевод без утечки данных (без отправки в интернет)
- Автоперевод архивов
'''

import argostranslate.package, argostranslate.translate
import pdfplumber
import docx2txt
import os

def load_model(from_code="en", to_code="ru"):
    installed_languages = argostranslate.translate.get_installed_languages()
    from_lang = next(filter(lambda l: l.code == from_code, installed_languages), None)
    to_lang = next(filter(lambda l: l.code == to_code, installed_languages), None)
    return from_lang.get_translation(to_lang) if from_lang and to_lang else None

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            return "\n".join(page.extract_text() or "" for page in pdf.pages)
    elif file_path.endswith(".docx"):
        return docx2txt.process(file_path)
    elif file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        raise ValueError("Неподдерживаемый формат")

def save_text(text, out_path):
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)

# Пример использования
file_path = "test_en.txt"
out_path = "translated_ru.txt"
translation = load_model("en", "ru")
text = extract_text(file_path)
translated = translation.translate(text)
save_text(translated, out_path)
print(f"✅ Перевод сохранён: {out_path}")
