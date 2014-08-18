#==============================
#run this to translate wiki artitle titles in English to Chinese
#was used to translate university name, but not limit to it
#==============================

import sys
import json
import urllib2
import string

college_name = string.capwords(str(sys.argv[1]))
college_name = college_name.replace(" ", "%20")

url = "http://en.wikipedia.org/w/api.php?format=json&action=query&titles=" + college_name + "&prop=langlinks&lllang=zh"
jsonurl = urllib2.urlopen(url)
data = json.loads(jsonurl.read())
for key in data['query']['pages']:
	print data['query']['pages'][key]['langlinks'][0]['*']
