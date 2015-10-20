# -*-coding:utf-8-*-
__author__ = 'Administrator'


def lines(file):
    with open(file) as f:
        content_lines = f.readlines()
    return content_lines


def blocks(file):
    line_list = lines(file)
    str = ''.join(line_list)
    new_list = str.split('\n\n')
    return new_list


def line_gen(file):
    for line in file:
        yield line
        yield '\n'


def blocks_gen(file):
    text_block = []
    for line in line_gen(file):
        if line.strip():
            text_block.append(line)
        elif text_block:
            yield ''.join(text_block).strip()
            text_block = []
