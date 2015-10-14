#-*-coding:utf-8-*-
__author__ = 'Administrator'

import re, sys
from util import *

print '<html><head><title>...</title><body>'

title = True

for text_block in blocks_gen(sys.stdin):
    text_block = re.sub(r'\*(.+?)\*', r'<em>\l</em>', text_block)
    if title:
        print '<h1>'
        print text_block
        print '</h1>'
        title = False
    else:
        print '<p>'
        print text_block
        print '</p>'

print '</body></html>'

