#!/usr/bin/python
import sys
sys.path.append("..")

import cgi
import cgitb
cgitb.enable()

from lib import template

title = 'Python Template Test'
body = '<h1>Jason Snider</h1>'

print('Content-type: text/html\n\n')
print(template.input(title, body))
