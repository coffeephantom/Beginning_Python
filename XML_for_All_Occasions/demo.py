from xml.sax.handler import ContentHandler
from xml.sax import parse

__author__ = 'coffeephantom'


class TestHandler(ContentHandler):
    def startElement(self, name, attrs):
        print name, attrs.keys()

if __name__ == '__main__':
    parse('website.xml', TestHandler())