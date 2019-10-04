#!/usr/bin/python
import sys
sys.path.append("../..")
from lib import template

import cgi
import cgitb
cgitb.enable()
import pymysql

title = 'Blog'
body = '<h1>Jason Snider\'s Blog</h1>'

print('Content-type: text/html\n\n')



# Connect to the database.

conn = pymysql.connect(
    db='jasonsnider',
    user='root',
    passwd='password',
    host='localhost')
c = conn.cursor()

c.execute("SELECT * FROM articles")

for r in c.fetchall():
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
