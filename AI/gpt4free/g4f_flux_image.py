# conda activate extras2

from g4f.client import Client

client = Client()
'''
response = client.images.generate(
    model="flux",
    prompt="a professional photo of beautiful young woman with blue eyes",
    response_format="url"
)
'''
response = client.images.generate(
    model="flux",
    prompt="a professional photo of beautiful young woman with blue eyes"
)

#print(f"Generated image URL: {response.data[0].url}")

'''
Если в параметрах client отсутствует response_format, то картинки сохраняются в папку generated_images в одной папке 
со скриптом/
---------------------
При response_format="url"

Generated image URL: https://image.pollinations.ai/prompt/a+white+siamese+cat?seed=42162458&width=1024&height=1024&
model=flux&nologo=true&private=false&enhance=false&safe=false
'''