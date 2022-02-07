
import requests
import dominate
import json
from dominate.tags import *

r = requests.get('http://localhost/articles')
data = r.json()
doc = dominate.document(title='Articles')

with doc:
    with div():
        attr(cls='body')
        for item in data:
            p(json.dumps(item))


with open('first.html', 'w') as f:
    f.write(doc.render())

