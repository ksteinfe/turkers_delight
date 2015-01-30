#Collate.py looks at a culled image folder and the available index jsons and creates a new master json.
import glob, json, re

#new dict add {"filename": filename}
#load all the img names into an array
dir = "Images/*"

Filenames = [g[7:] for g in (glob.glob(dir))]
IndexFilenames = [j for j in glob.glob('*.json') if ('ErrorReport' , 'Collated' not in j)]
Indices_Collated = []
Indices_Culled = []

for ifilename in IndexFilenames:
	with open (ifilename) as json_file:
		index_items = json.load(json_file)
		json_file.close()
	[Indices_Collated.append(i) for i in index_items]

print len (Indices_Collated)
print len (Filenames)



for filename in Filenames:
	#print filename
	namechunks = re.split('_', filename)
	#print namechunks
	type = unicode(namechunks[0])
	keyword = unicode(namechunks[1])
	id = unicode(namechunks[2].translate(None, 'jpgifnbmeJPGIFNBME.'))
	#print id
	[Indices_Culled.append(c) for c in Indices_Collated if (c['type'] == type and c['keyword'] == keyword and c['id'] == id) ]

print Indices_Collated[125]
print len (Indices_Culled)

with open ('Culled_Index.json', 'w') as json_file:
	json_file.write(json.dumps(Indices_Culled))
	json_file.close()