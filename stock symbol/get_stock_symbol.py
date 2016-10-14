#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import re
import os
from bs4 import *


def make_soup(i):
    url = 'http://isin.twse.com.tw/isin/C_public.jsp?strMode='
    tmp = url + i
    html = urllib2.urlopen(tmp).read()
    soup = BeautifulSoup(html, from_encoding='big5')
    return soup


def strMode():
    for i in ['1', '2', '3', '4', '5']:
        soup = make_soup(i)
        print soup.font.string
        tag = soup('td')

        for item in tag:
            if item.contents != [] and isinstance(item.contents[0], basestring):
                if re.match('\d+\s+.+', item.contents[0]):
                    (symbol, name) = item.contents[0].split()
                    print symbol, '\t', name


def main():
    strMode()


if __name__ == '__main__':
    main()
