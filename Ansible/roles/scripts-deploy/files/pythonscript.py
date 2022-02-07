#!/usr/bin/python3
import requests
import dominate
import json
from dominate.tags import *

r = requests.get('http://localhost/app/articles')
data = r.json()
doc = dominate.document(title='Articles')

with doc:
    with div():
        attr(cls='body')
        for item in data:
            p(json.dumps(item))


with open('/var/www/html/index.html', 'w') as f:
    f.write(doc.render())

