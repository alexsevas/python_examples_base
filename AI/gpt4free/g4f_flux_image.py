from g4f.client import Client

client = Client()
response = client.images.generate(
    model="flux",
    prompt="a white siamese cat",
    response_format="url"
)

print(f"Generated image URL: {response.data[0].url}")

'''
Generated image URL: https://image.pollinations.ai/prompt/a+white+siamese+cat?seed=42162458&width=1024&height=1024&
model=flux&nologo=true&private=false&enhance=false&safe=false
'''