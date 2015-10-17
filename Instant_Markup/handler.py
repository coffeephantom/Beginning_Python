# -*-coding:utf-8-*-

import re

__author__ = 'coffeephantom'


class HTMLParser:
    def start_doc(self):
        print '<html><head><title>...</title></head><body>'

    def end_doc(self):
        print '</body></html>'

    def start_title(self):
        print '<h1>'

    def end_title(self):
        print '</h1>'

    def start_em(self):
        print '<em>'

    def end_em(self):
        print '</em>'

    def start_para(self):
        print '<p>'

    def end_para(self):
        print '</p>'
