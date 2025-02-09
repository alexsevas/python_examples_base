# pip install SpeechRecognition pyttsx3 openai
# SpeechRecognition для распознавания речи требует подключение к инету

# ENV allpy310

import speech_recognition as sr
import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            return text.lower()
        except sr.UnknownValueError:
            speak_text("Sorry, I didn't understand that.")
            return None
        except sr.RequestError:
            speak_text("Network error, please check your connection.")
            return None

if __name__ == "__main__":
    speak_text("Hello! How can I help you?")
    command = recognize_speech()
    if command:
        speak_text(f"You said: {command}")