# ENV allpy310

# pip install translators

from translators.server import translate

text = "Hello, how are you?"
translated_text = translate(text, from_language="en", to_language="fr", engine="google")
print(translated_text)  # "Bonjour, comment ça va ?"
