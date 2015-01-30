import requests, json, urllib, cStringIO
from bs4 import BeautifulSoup
from PIL import Image

save_path='imgs/'
download_images = False
limit_results = 2000

"""
Get the HTML of the main page and parse in BeautifulSoup
"""
url = 'designguggenheimhelsinki.org/stageonegallery/view/'
rdata = requests.get('http://'+ url).text
soup=BeautifulSoup(rdata, "html5lib")


"""
Gather up all the links to individual design pages
"""
design_ids = []

# for each link found on the page
for link in soup.find_all('a'):
    design_link = str(link.get('href'))
    if 'gh-' in design_link:
        design_id = design_link[22:]
        design_ids.append(design_id)

print "found ", len(design_ids), " design links"


"""
Visit each design page, constructing a dictionary for each.
"""

designs={}

for id in design_ids[:limit_results]:
    print "loading page", id
    design_dict = {}
    rdata = requests.get('http://'+ url + id).text
    soup = BeautifulSoup(rdata)
    img_tags = soup.find_all('img')
    if len(img_tags)==2: 
        src0 = img_tags[0].get('src')
        src1 = img_tags[1].get('src')
        design_dict['imgs']= (src0,src1)
        designs[id] = design_dict
    else:
        print "didn't find two images on this page", id
    
print "found two images on each of ", len(designs), " pages"


"""
Write the summary JSON
"""
with open('_summary.json', 'w') as j:
	j.write(json.dumps(designs))
	j.close()

            
"""
Download the images we found to a local directory
"""
if download_images:
    for id, design in designs.items():
        print "downloading images from page", id
        try:
            src_url = design['imgs'][0]
            dest_path = save_path + id + "_C0.jpg"
            urllib.urlretrieve(src_url, dest_path)
            
            src_url = design['imgs'][1]
            dest_path = save_path + id + "_C1.jpg"
            urllib.urlretrieve(src_url, dest_path)
        except:
            print "error in downloading images from design", id

            
            
            
            
            
            
            