from xml.sax.handler import ContentHandler
from xml.sax import parse

__author__ = 'coffeephantom'


class TestHandler(ContentHandler):
    def startElement(self, name, attrs):
        print name, attrs.keys()


class HeadlineHandler(ContentHandler):
    in_headline = False
    def __init__(self, headlines):
        ContentHandler.__init__(self)
        self.headlines = headlines
        self.data = []

    def startElement(self, name, attrs):
        if name == 'h1':
            self.in_headline = True

    def endElement(self, name):
        if name == 'h1':
            text = ''.join(self.data)
            self.data = []
            self.headlines.append(text)
            self.in_headline = False

    def characters(self, content):
        if self.in_headline:
            self.data.append(content)


if __name__ == '__main__':
    headlines = []
    parse('website.xml',HeadlineHandler(headlines))
    print 'The following <h1> elements was found'
    for h in headlines:
        print h