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
        <nav>
            <a href="/">Home</a>
            <a href="/resume.py">Resume</a>
        </nav>
        {body}
    </body>
</html>\
'''.format(
    title=title, 
    body=body
).strip()