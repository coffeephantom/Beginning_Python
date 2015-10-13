#-*-coding:utf-8-*-
__author__ = 'Administrator'

def lines(file):
    with open(file) as f:
        content_lines = f.readlines()
    return content_lines


def block(file):
    line_list = lines(file)
    str = ''.join(line_list)
    new_list = str.split('\n\n')
    return new_list



