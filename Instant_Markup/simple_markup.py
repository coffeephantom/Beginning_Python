import sys, re
__author__ = 'Administrator'

from util import *


def markup(file):
    new_content = ['<html><head><title>...</title><body>']
    title = True
    for block_element in block(file):
        block_element = re.sub(r'\*(.+?)\*', r'<em>\l</em>', block_element)
        if title:
            new_content.append('<h1>')
            new_content.append(block_element)
            new_content.append('</h1>')
            title = False
        else:
            new_content.append('<p>')
            new_content.append(block_element)
            new_content.append('<p>')
    new_content.append('</body></html>')
    return new_content

if __name__ == '__main__':
    print markup('text_input.txt')

