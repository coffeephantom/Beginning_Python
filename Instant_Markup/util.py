#-*-coding:utf-8-*-
__author__ = 'Administrator'

def lines(file):
    with open(file) as f:
        content_lines = f.readline()
    return content_lines

