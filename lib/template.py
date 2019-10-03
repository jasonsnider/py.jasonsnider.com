#!/usr/bin/python

from textwrap import dedent

def input(title, body):
    title = title
    body = body

    return '''\
<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>{title}</title>
    </head>
    <body>
        <h1>{title}</h1>
        {body}
    </body>
</html>\
'''.format(
    title=title, 
    body=body
).strip()