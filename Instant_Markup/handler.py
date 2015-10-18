# -*-coding:utf-8-*-

import re

__author__ = 'coffeephantom'


class HTMLParser(Handler):

    def start_doc(self):
        print '<html><head><title>...</title></head><body>'

    def end_doc(self):
        print '</body></html>'

    def start_title(self):
        print '<h1>'

    def end_title(self):
        print '</h1>'

    def sub_emphasis(self, match):
        return '<em>%s</em>' % match.group(1)

    def start_paragraph(self):
        print '<p>'

    def end_paragraph(self):
        print '</p>'

class Handler:

    def callback(self, prefix, name, *args):
        method = getattr(self, prefix+name, None)
        if callable(method):
            return method(*args)

    def start(self, name):
        self.callback('start_', name)

    def end(self, name):
        self.callback('end_', name)


    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None:
                match.group(0)
            return result
        return substitution

