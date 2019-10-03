#!/usr/bin/python
import sys
sys.path.append("..")

import cgi
import cgitb
cgitb.enable()

from lib import template

title = 'Jason Snider\'s Resume'
body ='''\
    <h1>Jason Snider</h1>
    <h2>Builder of Things, Doer of Stuff</h2>
\
'''.strip()

print('Content-type: text/html\n\n')
print(template.input(title, body))
