__author__ = 'coffeephantom'

class Rule:
    def action(self, block, handler):
        handler.start(self, type)
        handler.feed(block)
        handler.end(self, type)
        return True

class HeadlineRule(Rlue):
    def condition(self, block):
        return not '\n' in block and len(block) <= 70 and not block[-1] == ':'


class TitleRule(HeadlineRule):
    type = 'titile'
    first = True

    def condition(self, block):
        if not self.first:
            return False
        self.first = False
        return HeadlineRule.condition(self, block)

class ListItemRule(Rule):
    type = 'listitem'

    def condition(self, block):
        return block[0] = '-'
    def action(self, block, handler):
        handler.start(self, type)
        handler.feed(block[1:].strip())
        handler.end(self, type)