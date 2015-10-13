import sys, re
__author__ = 'Administrator'

from util import *

print '<html><head><title>...</title><body>'

def markup(file):
    title = True
    for block_element in block(file):
        block_element = re.sub(r'\*(.+?)\*', r'<em>\l</em>', block_element)
        if title:
            print '<h1>'
            print block_element
            print '</h1>'
            title = False
        else:
            print '<p>'
            print block_element
            print '</p>'
        print '</body></html>'

if __name__ == '__main__':
    markup('text_input.txt')

