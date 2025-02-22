# ENV allpy310
# pip install translators
# pip install --upgrade translators


from translators.server import translate_text  #fix - метод translate устарел
# pip install --upgrade translators

text = "Hello, how are you?"
translated_text = translate_text(text, from_language="en", to_language="fr", engine="google")
print(translated_text)  # "Bonjour, comment ça va ?"
