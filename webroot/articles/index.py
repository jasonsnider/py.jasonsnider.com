#!/usr/bin/python
import sys
sys.path.append("../..")
from lib import template
from lib.models.articles import Articles

import cgi
import cgitb
cgitb.enable()

title = 'Blog'
body = '<h1>Jason Snider\'s Blog</h1>'

print('Content-type: text/html\n\n')

articles = Articles()

for r in articles.fetchArticles():
    body = body + '''\
<a href="/articles/view/{slug}">
    <h2>{title}</h2>
    <p>{description}</p>
</a><hr>\
'''.format(
    slug=r[1],
    title=r[2],
    description=r[4]
)

print(template.input(title, body))
