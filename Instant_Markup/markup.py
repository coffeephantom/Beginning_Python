__author__ = 'coffeephantom'

import sys, re
from handler import *
from util import *
from rules import *


class Parser:
    def __init__(self):
        self.handler = handler
        self.rule = rules
        self.filters = []

    def addRule(self, rule):
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        self.handler.start('document')
        for block in blocks_gen(file):
            for filter in self.filters:
                block = filter(block, self.handler)

            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last:
                        break
        self.handler.end('document')


