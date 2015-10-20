import sys, re
__author__ = 'Administrator'

from util import *


def markup(file):
    new_content = ['<html><head><title>...</title><body>']
    title = True
    for block_element in blocks(file):
        block_element = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block_element)
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


def output(content, file):
    with open(file, 'w') as f:
        f.writelines(content)

if __name__ == '__main__':
    output(markup('text_input.txt'), 'text.output2.html')
