import urllib
import urllib2

__author__ = 'Administrator'


def get_data(url):
   url_content = urllib2.urlopen(url)
   data = url_content.read()
   return data

def save_data(data, filename):
   with open(filename, 'wb') as f:
      f.write(data)


if __name__ == '__main__':
   data = get_data('ftp://ftp.swpc.noaa.gov/pub/weekly/Predict.txt')
   save_data(data, 'data.txt')
