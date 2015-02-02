import requests, json, urllib
from bs4 import *


"""
Get the HTML of the main page and parse in BeautifulSoup
"""
url = 'designguggenheimhelsinki.org/stageonegallery/view/'
rdata = requests.get('http://'+ url).text
soup=BeautifulSoup(rdata, "html5lib")

"""
Load in the existing summary JSON
"""
with open('_summary.json') as json_data:
	summary = json.load(json_data)
	json_data.close()

    
    
"""
<li class="item visible t-straight t-square t-concrete t-opaque t-textured ">
    <a href="/stageonegallery/view/gh-2551962544" class="shortlist-entry-link " data-id="gh-2551962544">
        <img class="lazy" data-scale="2" data-original="http://a2.designguggenheimhelsinki.org/GH-2551962544-partC1.jpg" alt="" src="http://a2.designguggenheimhelsinki.org/GH-2551962544-partC1.jpg" style="display: block; transform: none;">
    </a>
</li>
"""

tag_dict = {}

for list_item in soup.find_all('li'):
    label = list_item.get('class')
    print label
    try: 
		id = str(list_item.a.get('data-id'))
		projectTags = label[2:]
		projectTagsConverted = [str(t) for t in projectTags]
		tag_dict[id] = [t[2:] for t in projectTagsConverted if len(t) > 1]
    except: print ('error')

    
"""
#print tag_dict
summary_dict = dict((k.encode('ascii'), v) for (k, v) in summary.items())
#print summary_dict
for entry in summary_dict:
	summary_dict[entry] = dict((k.encode('ascii'), v.encode('ascii')) for (k, v) in summary_dict[entry].items())

for entry in summary_dict:
	tags = tag_dict[entry]
	#print entry
	#print tags
	summary_dict[entry]['tags'] = tags

print len(summary_dict)



with open('summary_wtags.json', 'w') as j:
	j.write(json.dumps(summary_dict))
	j.close()

	
"""