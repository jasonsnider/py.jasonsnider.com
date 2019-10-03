#!/usr/bin/python
import sys
sys.path.append("..")

import cgi
import cgitb
cgitb.enable()

from lib import template

title = 'Python Template Test'
body = '<p>Sweet, sweet, PY!</p>'

print('Content-type: text/html\n\n')
print(template.input(title, body))
