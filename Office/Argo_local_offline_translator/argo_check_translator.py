

from argostranslate import translate

# Загрузка модели (автоматически при первом запуске)
installed_languages = translate.get_installed_languages()
source_lang = installed_languages[0]  # например, английский
target_lang = installed_languages[1]  # например, русский

# Перевод текста
translation = source_lang.get_translation(target_lang)
result = translation.translate("Hello, world!")
print(result)  # "Привет, мир!"