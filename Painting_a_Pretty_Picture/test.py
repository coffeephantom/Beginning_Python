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

def pre_process_data(filename):
   with open(filename, 'rb') as f:
      data_li = f.readlines()
      return data_li




if __name__ == '__main__':
   print pre_process_data('data.txt')