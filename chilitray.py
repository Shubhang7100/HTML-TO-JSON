import json
from bs4 import BeautifulSoup
import requests
from importlib.resources import contents
from urllib.request import urlopen
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://getlatka.com/'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
results = []

# Retrieve all of the data
for tag in soup.recursiveChildGenerator():
    if tag.name is None and not tag.isspace():
        results.append({
            'TAG': tag.parent.name,
            'ATTRIBUTES': tag.parent.attrs
        })

#saving in the JSON format
with open('final.json','w') as json_file:
    json_file.write(json.dumps(results,indent=2))
