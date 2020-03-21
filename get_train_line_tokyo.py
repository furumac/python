from lxml import etree
import requests
import random

pref = '13' # Tokyo 
baseuri='http://www.ekidata.jp/api/p/'
uri = baseuri + pref + '.xml'
headers = {'content-type': 'text/xml'}
response = requests.get(
  uri,
  headers=headers)
root = etree.fromstring(response.content)

def main():
    index = 0
    line_cd = {}
    line_name = {}
    for line in root.xpath('//line'):
        line_cd[index] = line.findtext('line_cd')
        line_name[index] = line.findtext('line_name')
        index += 1

    rand_int = (random.randint(0, len(line_cd)-1))
    print(line_name[rand_int])

if __name__ == '__main__':
    main()
