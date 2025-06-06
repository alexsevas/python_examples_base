# conda activate allpy310

# python 3.9+
# pip install -q -U google-genai

from google import genai
import os
import dotenv

dotenv.load_dotenv()
GENAI_API = os.getenv('GENAI_API')

client = genai.Client(api_key=GENAI_API)

my_file = client.files.upload(path="data/picture01.jpg")

prompt = (
    'You are the vision analysis AI that provides semantic meaning from images to provide context '
    'to send to another AI that will create a response to the user. Do not respond as the AI assistant '
    'to the user. Instead take the user prompt input and try to extract all meaning from the photo '
    'relevant to the user prompt. Then generate as much objective data about the image for the AI '
    f'assistant who will respond to the user. Свой ответ сразу переводи на русский язык'
)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[my_file, prompt],
    #contents=[my_file, "Caption this image."],
)

print(response.text)