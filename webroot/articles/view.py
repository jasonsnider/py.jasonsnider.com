#!/usr/bin/python
import sys
sys.path.append("../..")
from lib import template
from lib.models.articles import Articles

import cgi
import cgitb
cgitb.enable()

# Parse Get params
fieldStorage = cgi.FieldStorage()
params = {}
for key in fieldStorage.keys():
    params[key] = fieldStorage[key].value

# Instantiate Articles 
articles = Articles()

slug = 'test'
r = articles.fetchArticle(params['slug'])

title = r[3]

body = '''\
<h1>{title}</h1>
{body}\
'''.format(
    title=r[3],
    body=r[5]
)

# Set the page header
print('Content-type: text/html\n\n')
print(template.input(title, body))
