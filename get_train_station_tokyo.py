from lxml import etree
import requests
import random

pref = '13' # Tokyo 
baseuri_pref = 'http://www.ekidata.jp/api/p/'
baseuri_line = 'http://www.ekidata.jp/api/l/'
uri_pref = baseuri_pref + pref + '.xml'
headers = {'content-type': 'text/xml'}
response = requests.get(
  uri_pref,
  headers=headers)
root = etree.fromstring(response.content)

def main():
    i = 0
    line_cd = {}
    line_name = {}
    for line in root.xpath('//line'):
        line_cd[i] = line.findtext('line_cd')
        line_name[i] = line.findtext('line_name')
        i += 1

    rand_i = (random.randint(0, len(line_cd)-1))
    target_line_cd = line_cd[rand_i]
    target_line_name = line_name[rand_i]
    uri_line = baseuri_line + target_line_cd + '.xml'

    response = requests.get(
        uri_line,
        headers=headers)
    l_root = etree.fromstring(response.content)

    j = 0
    station_name = {}
    for line in l_root.xpath('//station'):
        station_name[j] = line.findtext('station_name')
        j += 1

    rand_j = (random.randint(0, len(station_name)-1))
    target_station_name = station_name[rand_j]

    print("今回注目する駅は「" + target_line_name +
            "」の「" + target_station_name + "」駅です")

    

if __name__ == '__main__':
    main()
