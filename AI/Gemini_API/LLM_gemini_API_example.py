# conda activate allpy310

# python 3.9+
# pip install -q -U google-genai

from google import genai
import os
import dotenv

dotenv.load_dotenv()
GENAI_API = os.getenv('GENAI_API')

client = genai.Client(api_key=GENAI_API)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="В чем смысл жизни людей?",
)

print(response.text)