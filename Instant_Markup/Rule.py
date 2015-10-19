__author__ = 'coffeephantom'

class Rule:
    def action(self, block, handler):
        handler.start(self, type)
        handler.feed(block)
        handler.end(self, type)
        return True

class HeadlineRule:
    def condition(self, block):
        pass

