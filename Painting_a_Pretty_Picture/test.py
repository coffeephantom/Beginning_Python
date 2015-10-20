import urllib
import urllib2
import reportlab
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF

__author__ = 'Administrator'


data = [
   (2015, 04, 53.0, 54.0, 52.0,127.6, 128.6, 126.6),
(2015, 05, 52.2, 54.2, 50.2, 123.9, 124.9, 122.9),
(2015, 06, 50.6, 53.6, 47.6, 119.8, 121.8, 117.8),
(2015, 07, 49.0, 54.0, 44.0, 116.3, 119.3, 113.3),
(2015, 08, 48.6, 53.6, 43.6, 113.8, 117.8, 109.8),
(2015, 09, 49.3, 55.3, 43.3, 111.8, 115.8, 107.8)
]

def get_data(url):
   url_content = urllib2.urlopen(url)
   data = url_content.read()
   return data

def save_data(data, filename):
   with open(filename, 'wb') as f:
      f.write(data)

def pre_process_data(filename):
   with open(filename, 'rb') as f:
      data_li = f.readlines()
      return data_li




if __name__ == '__main__':
   print pre_process_data('data.txt')