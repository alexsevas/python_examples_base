from argostranslate import package, translate
import pprint

# Проверка доступных языков
pprint.pprint(package.get_available_packages())