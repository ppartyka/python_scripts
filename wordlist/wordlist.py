#!/usr/bin/python

import urllib
from HTMLParser import HTMLParser
from sys import argv

script, url, fn = argv

text = ""
webfile1 = argv[2] + '.html'
webfile2 = open(webfile1, 'w+')

class MLStripper(HTMLParser):
    def __init__(self):
		self.reset()
		self.fed = []

    def handle_data(self, d):
	    self.fed.append(d)

    def get_data(self):
	    return ''.join(self.fed)


def strip_tags(html):
	s = MLStripper()
	s.feed(html)
	return s.get_data()

if __name__ == '__main__':
	urllib.urlretrieve(argv[1], filename=webfile1)

	try:
		text = webfile2.read()
	finally:
		webfile2.close()

	nohtml = strip_tags(text)

	for punc in '-<>\\/"[]{},.:;_=|()\'?+':
		nohtml = nohtml.replace(punc, '')

	nohtml = set(nohtml.lower().split())

	for x in nohtml:
		print x
