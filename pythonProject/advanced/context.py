from urllib import request
from xml.etree import ElementTree as ET
import json
import csv


def parse():
    feed = request.urlopen("http://pypi.python.org/pypi?:action=rss").read()
    rss = ET.fromstring(feed)
    w = csv.writer(open('parser.csv', 'a'), delimiter=' ')
    for item in rss.findall('channel/item'):
        try:
            date = item.findtext('pubDate')
            package, version = item.findtext('title').split()
            description = item.findtext('description')
            w.writerow((date, package, version, description))
        except:
            pass

def ex2():
    feed = request.urlopen("http://api.geonames.org/hierarchyJSON?formatted=true&geonameId=2657896&username=demo&style=full")
    json.load(feed)
