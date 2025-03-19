# conda activate extras2

from g4f.client import Client
from pprint import pprint

client = Client()

response = client.images.generate(
    model="flux",
    prompt="a professional photo of beautiful young woman with blue eyes",
    response_format="b64_json"
    # Add any other necessary parameters
)

base64_text = response.data[0].b64_json
pprint(base64_text)