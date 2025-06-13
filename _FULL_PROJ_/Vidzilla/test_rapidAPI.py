# conda activate py311v02

import http.client
import pprint
import os
from dotenv import load_dotenv

load_dotenv()
RAPIDAPI_KEY = os.getenv('RAPIDAPI_KEY')
MY_RAPID_WEB = os.getenv('MY_RAPID_WEB')
URL = "/free/gstin/"+MY_RAPID_WEB
print (URL)

conn = http.client.HTTPSConnection("gst-return-status.p.rapidapi.com")

headers = {
    'x-rapidapi-key': RAPIDAPI_KEY,
    'x-rapidapi-host': "gst-return-status.p.rapidapi.com",
    'Content-Type': "application/json"
}

conn.request("GET", URL, headers=headers)

res = conn.getresponse()
pprint.pprint(res.status)
data = res.read()

pprint.pprint(data.decode("utf-8"))

'''
451
('{"messages":"Sorry, we are unable to provide RapidAPI services to your '
 'location. RapidAPI is required to comply with US laws that restrict the use '
 'of our services in embargoed countries. If you believe you receiving this '
 'message in error, please contact support@rapidapi.com."}')
'''