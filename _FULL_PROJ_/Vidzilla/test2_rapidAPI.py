# conda activate py311v02

import requests
import pprint
import os
from dotenv import load_dotenv

'''
этот способ работает и выдает json
docs СМ - https://gst.jamku.app/apidocs
'''

load_dotenv()
RAPIDAPI_KEY = os.getenv('RAPIDAPI_KEY')
MY_RAPID_WEB = os.getenv('MY_RAPID_WEB')
url = "https://gst-return-status.p.rapidapi.com/free/gstin/"+MY_RAPID_WEB
print (url)

headers = {
	"x-rapidapi-key": RAPIDAPI_KEY,
	"x-rapidapi-host": "gst-return-status.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

pprint.pprint(response.json())